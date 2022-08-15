import strawberry
from typing import Optional

@strawberry.type
class Event:
    id: int
    title: str
    description: Optional[str]
    createdAt: str
    updatedAt: str
    
    @classmethod
    def from_instance(cls, instance: dict):
        return cls(
            id = instance['id'],
            title = instance['title'],
            description = instance["description"],
            createdAt = instance['createdAt'],
            updatedAt = instance['updatedAt']
        )


