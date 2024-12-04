from ninja import Schema


class UserLocation(Schema):
    id: int
    lat: float
    lon: float


class UsernameEmailSchema(Schema):
    username: str
    email: str


class EmailPinSchema(Schema):
    email: str
    pin: int
