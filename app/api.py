from django.db.models import Q
from django.core.cache import cache
from ninja import NinjaAPI
from ninja.responses import Response

from .models import User, Connection
from app import schema


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

def build_connection_list(connection, connections: list):
    return connections.append({
        "id": connection.id,
        "username": connection.username,
        "email": connection.email,
        "lat": connection.lat,
        "lon": connection.lon,
        "last_online": connection.last_online
    })

@api.get("/get-connections")
def get_connections(request, user_id: int):
    try:
        connection_query = Connection.objects.filter(
            Q(user_from=user_id) | Q(user_to=user_id)
        )
    except Connection.DoesNotExist:
        return 404

    connections = []
    for row in connection_query:
        if row.user_from.id != user_id:
            connection = row.user_from

        elif row.user_to.id != user_id:
            connection = row.user_to

        else:
            continue

        build_connection_list(connection, connections)

    return connections


@api.post("/update-user-location")
def update_user_location(request, UserLocation: schema.UserLocation):
    try:
        user = User.objects.get(id=UserLocation.id)
    except User.DoesNotExist:
        return Response({"error": "User Not Found"}, status=404)

    try:
        user.lat = UserLocation.lat
        user.lon = UserLocation.lon
        user.save()
    except Exception as error:
        print(error)

    return Response({"success": f"{user.id} {user.username} location updated"}, status=200)
