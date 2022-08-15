import strawberry
from strawberry.types import Info

@strawberry.type
class MediaQuery:

    @strawberry.field
    def all_media(self, info: Info ):
        request = info.context["request"]
        