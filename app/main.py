from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from requests_toolbelt.multipart import MultipartEncoder
from strawberry.fastapi import GraphQLRouter
from typing import List
from queries import Query
from mutations import Mutation
from media.resolvers import upload_files
import json

app = FastAPI()


@app.post("/api/upload")
async def submitForm(request: Request, refId: str = Form(...), ref: str=Form(...), field: str = Form(...), files: List[UploadFile] = File(...)):
  contents = []
  for file in files:
    contents.append(file.file)
  
  fields= {
      'refId': refId,
      'ref': ref,
      'field': field,
      'files': json.dumps(contents)
    }
  upload_files(fields, files, request.headers)

    


origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema)

app.include_router(graphql_app, prefix="/graphql")
app.add_websocket_route('/graphql', graphql_app)
