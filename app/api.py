from ninja import NinjaAPI, Schema

from .models import User


api = NinjaAPI()

@api.get("/get-user")
def get_user(request, id: int):
    print(id)
    try:
        user = User.objects.get(id=id)
        print(user)
    except User.DoesNotExist:
        return 404

    response = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "lat": user.lat,
        "lon": user.lon,
        "last_online": user.last_online
    }

    return response
