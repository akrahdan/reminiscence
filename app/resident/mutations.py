import strawberry
from strawberry.types import Info
from .definitions import Resident
from .resolvers import create_resident

@strawberry.input
class ResidentInput:
    ResidentId: str
    RoomNo: str

@strawberry.type
class ResidentMutation:

    @strawberry.mutation
    async def add_resident(self, resident: ResidentInput, info: Info) -> Resident:
        request = info.context["request"]
        res = await create_resident(resident, headers=request.headers)
        return Resident.from_instance(res)
