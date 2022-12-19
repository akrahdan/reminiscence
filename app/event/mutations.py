import strawberry
from typing import Optional
from strawberry.types import Info
from .definitions import Event
from .resolvers import create_event, delete_event

@strawberry.input
class EventInput:
    Title: str
    Description: Optional[str]
    resident: int

@strawberry.type
class EventMutation:

    @strawberry.mutation
    async def add_event(self, event: EventInput, info: Info) -> Event:
        request = info.context["request"]
        res = await create_event(event=event, headers=request.headers)
        return Event.from_instance(res)
    
    @strawberry.mutation
    async def delete_event(self, id: int, info: Info) -> Event:
        request = info.context["request"]
        res = await delete_event(uid=id, headers=request.headers)
        return Event(id=res, title="", description="")

