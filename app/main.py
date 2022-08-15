from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from queries import Query
from mutations import Mutation
app = FastAPI()

origins = [
    "http://localhost:3000"
]
app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers=["*"]

)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema)

app.include_router(graphql_app, prefix="/graphql")
app.add_websocket_route('/graphql', graphql_app)

