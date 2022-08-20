from multiprocessing.util import info
import strawberry
from strawberry.types import Info
from typing  import List,  Optional
from .definitions import Event
from .resolvers import load_events

@strawberry.type
class EventQuery:
    @strawberry.field
    async def all_events(self, info: Info) -> List[Event]:
        request = info.context['request']
    
        events = await load_events(header=request.headers)
        print("Events: ", [Event.from_instance(event) for event in events])

        # return [Event(id=1, title="Gogog", description="d",createdAt="", updatedAt="", photos=None)]
        return [Event.from_instance(event) for event in events]
