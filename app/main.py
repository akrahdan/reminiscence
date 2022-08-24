from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import strawberry

from strawberry.fastapi import GraphQLRouter
from pathlib import Path
from queries import Query
from mutations import Mutation

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()


@app.get("/api/upload/{rest:path}")
async def fetch_file(request: Request, rest:str):
  filename = f'event/upload/{rest}'
  path = BASE_DIR.joinpath(filename)
  return FileResponse(path=path)
  

    


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
