from ninja import Schema


class UserLocation(Schema):
    id: int
    lat: float
    lon: float
