from multiprocessing.util import info
import strawberry
from strawberry.types import Info
from typing  import List,  Optional
from .definitions import Event
from .resolvers import load_events

@strawberry.type
class EventQuery:
    @strawberry.field
    def all_events(self, info: Info) -> List[Event]:
        request = info.context['request']
        events = load_events(headers=request.headers)
        return [Event.from_instance(event) for event in events]
