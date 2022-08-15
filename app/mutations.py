from strawberry.tools import merge_types
from resident.mutations import ResidentMutation
from event.mutations import EventMutation
from media.mutations import MediaMutation
from user.mutations import LoginMutation

Mutation = merge_types( "Mutation", (ResidentMutation, EventMutation,  MediaMutation, LoginMutation))