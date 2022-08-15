import strawberry
from typing import Optional

@strawberry.type
class User:
    id: int
    username: str
    email: str
    jwt: Optional[str]

    @classmethod
    def from_instance(cls, instance):
        return cls(
            id=instance["id"],
            username=instance["username"],
            email=instance["email"],
            jwt = instance.get("jwt", None)
        )
