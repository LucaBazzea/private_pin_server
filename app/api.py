from django.db.models import Q
from django.core.cache import cache

from ninja import NinjaAPI
from ninja.responses import Response

from .models import User, Connection
from app import models, schema, services


api = NinjaAPI()

@api.post("/login/otp/send/")
def login_otp_send(request, data: schema.EmailSchema):
    pin = services.generate_pin()

    cache.set(f"otp:{data.email}", pin, timeout=600)

    if services.send_otp_email(data.email, pin):
        return Response({"success": "OTP Sent"}, status=200)


@api.post("/login/otp/validate/")
def login_otp_validate(request, data: schema.EmailPinSchema):
    pin_cached = cache.get(f"otp:{data.email}")

    if pin_cached is None:
        return Response({"error": "OTP Expired"}, status=400)

    if pin_cached != data.pin:
        return Response({"error": "Invalid OTP"}, status=400)

    try:
        user = User.objects.get(email=data.email)

    except User.DoesNotExist:
        username = data.email.split("@")[0]
        user = User(
            username=username,
            email=data.email,
        )
        user.save()

    # Username taken
    except User.IntegrityError:
        username = services.generate_username(data.email)
        user = User(
            username=username,
            email=data.email,
        )
        user.save()

    request.session["user_id"] = user.id

    return Response({"id": user.id}, status=200)


@api.post("/username/change/")
def username_change(request, username_new: str):
    try:
        user = User.objects.get(id=request.get("user_id"))
    except User.DoesNotExist:
        return Response({"error": "User Not Found"}, status=404)

    try:
        user.username = username_new
        user.save()
    except User.IntegrityError:
        return Response({"error": "Username Taken"}, status=400)

    return Response({"success": f"{user.id} {user.username} username updated"}, status=200)


@api.get("/logout/")
def logout(request):
    request.session.flush()
    return Response("Logout Success", status=200)


@api.get("/get-user/")
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

@api.get("/get-connections/")
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


@api.post("/update-user-location/")
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
