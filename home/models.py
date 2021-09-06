from django.db import models


class Subscriber(models.Model):
    user_email = models.EmailField(max_length=100)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.user_email