import strawberry
from typing import Optional

@strawberry.type
class Resident:
    id: int
    residentId: Optional[str]
    roomNo: Optional[str]
    createdAt: str
    updatedAt: str

    @classmethod
    def from_instance(cls, instance: dict):
        return cls(
            id = instance['id'],
            residentId = instance['residentId'],
            roomNo = instance["roomNo"],
            createdAt = instance['createdAt'],
            updatedAt = instance['updatedAt']
        )