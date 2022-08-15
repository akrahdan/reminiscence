import strawberry
from strawberry.types import Info
from .definitions import User
from .resolvers import user_login

@strawberry.input
class LoginInput:
    identifier: str
    password: str


@strawberry.type
class LoginMutation:
    
    @strawberry.mutation
    def login(self, input: LoginInput, info: Info) -> User:
        request = info.context["request"]
        print("Login: ", input.password)
        user = user_login(input, request.headers)
        return User.from_instance(user)
        