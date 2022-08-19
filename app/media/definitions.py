import strawberry
from typing import Optional

@strawberry.type
class Media:
    id: int
    name: str
    width: Optional[float]
    height: Optional[float]
    mime: str
    url: str

    @classmethod
    def from_instance(cls, instance: dict):
        return cls(
            id=instance['id'],
            name=instance['name'],
            width=instance.get("width", None),
            height=instance.get('height', None),
            mime=instance['mime'],
            url=instance['url']
        )
