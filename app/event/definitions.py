import strawberry
from typing import Optional, List
from media.definitions import Media
@strawberry.type
class Event:
    id: int
    title: str
    description: Optional[str]
    createdAt: str
    updatedAt: str
    photos: Optional[List[Media]]
    
    @classmethod
    def from_instance(cls, instance: dict):
        return cls(
            id = instance['id'],
            title = instance['title'],
            description = instance["description"],
            createdAt = instance['createdAt'],
            updatedAt = instance['updatedAt'],
            photos = [Media.from_instance(photo) for photo in instance["photos"]]
        )


