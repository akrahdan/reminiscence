import strawberry


@strawberry.type
class Media:
    id: int
    name: str
    width: float
    height: float
    mime: str
    url: str

    @classmethod
    def from_instance(cls, instance: dict):
        return cls(
            id=instance['id'],
            name=instance['name'],
            width=instance["width"],
            height=instance['height'],
            mime=instance['mime'],
            url=instance['url']
        )
