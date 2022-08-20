import strawberry
from strawberry.types import Info
from .resolvers import get_currrent_user
from .definitions import User

@strawberry.type
class UserQuery:
    
    @strawberry.field
    async def current_user(self, info: Info) -> User:
        request = info.context["request"]

        user = await get_currrent_user(request.headers)
        return User.from_instance(user)