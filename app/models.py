from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32) # TODO: limit which characters can be used
    email = models.EmailField()
    lat = models.FloatField(null=True) # TODO: PGP
    lon = models.FloatField(null=True) # TODO: PGP
    last_online = models.DateTimeField(null=True) # TODO: PGP
    created_at = models.DateTimeField(auto_now_add=True)


class Pod(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class PodMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    circle = models.ForeignKey(Pod, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
