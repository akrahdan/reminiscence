from strawberry.tools import merge_types
from event.queries import EventQuery
from resident.queries import ResidentQuery
from user.queries import UserQuery
Query = merge_types( "Query", (EventQuery, ResidentQuery, UserQuery))
