import strawberry
from typing import Optional
from strawberry.types import Info
from .definitions import Event
from .resolvers import create_event

@strawberry.input
class EventInput:
    Title: str
    Description: Optional[str]
    resident: int

@strawberry.type
class EventMutation:

    @strawberry.mutation
    def add_event(self, event: EventInput, info: Info) -> Event:
        request = info.context["request"]
        res = create_event(event=event, headers=request.headers)
        return Event.from_instance(res)
