from typing import List
import strawberry
from strawberry.types import Info
from .definitions import Resident
from .resolvers import load_residents

@strawberry.type
class ResidentQuery:

    @strawberry.field
    async def allResidents(self, info: Info) -> List[Resident]:
        request = info.context["request"]
        residents =  await load_residents(headers=request.headers)
        print("Resident: ", residents)

        # return [Resident(id =2, residentId="1233", roomNo="1223", createdAt="12345", updatedAt="222-2222")]
        return [Resident.from_instance(resident) for resident in residents]

