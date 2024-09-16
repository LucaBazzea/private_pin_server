from django.db.models import Q
from ninja import NinjaAPI, Schema

from .models import User, Connection


api = NinjaAPI()

@api.get("/get-user")
def get_user(request, id: int):
    try:
        user = User.objects.get(id=id)
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

@api.get("/get-connections")
def get_connections(request, user_id: int):
    try:
        connection_query = Connection.objects.filter(
            Q(user_from=user_id) | Q(user_to=user_id)
        )
    except Connection.DoesNotExist:
        return 404

    connections = []
    for connection in connection_query:
        if connection.user_from.id != user_id:
            connections.append(connection.user_from.id)
        elif connection.user_to.id != user_id:
            connections.append(connection.user_to.id)

    return connections
