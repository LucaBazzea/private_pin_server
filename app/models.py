from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32) # TODO: limit which characters can be used
    email = models.EmailField()
    lat = models.FloatField(null=True) # TODO: PGP
    lon = models.FloatField(null=True) # TODO: PGP
    last_online = models.DateTimeField(null=True) # TODO: PGP
    created_at = models.DateTimeField(auto_now_add=True)


class Connection(models.Model): # AKA: Friends list
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_from")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_from", "user_to")

    def remove_connection(self):
        self.delete()

    def __str__(self):
        return f"{self.user_from.username} :: {self.user_to.username}"


class ConnectionStatus(models.Model):
    CONNECTION_STATUS_CHOICES = [
        ("P", "Pending"),
        ("A", "Accepted"),
        ("D", "Declined"),
    ]
    connection = models.OneToOneField(Connection, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=CONNECTION_STATUS_CHOICES, default="P")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.connection.user_from.username} :: {self.connection.user_to.username} - {self.get_status_display()}"


class Pod(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class PodMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pod = models.ForeignKey(Pod, on_delete=models.PROTECT)
    joined = models.DateTimeField(auto_now_add=True)
