from typing import List
import strawberry
from strawberry.types import Info
from .definitions import Resident
from .resolvers import load_residents

@strawberry.type
class ResidentQuery:

    @strawberry.field
    def allResidents(self, info: Info) -> List[Resident]:
        request = info.context["request"]
        residents = load_residents(headers=request.headers)

        return [Resident.from_instance(resident) for resident in residents]

