from django.contrib import admin
from .models import Subscriber


class Email_Subscription(admin.ModelAdmin):
    fields = (
        'user_email',
        'subscribed',
    )

    list_display = (
        'user_email',
        'subscribed',)


admin.site.register(Subscriber, Email_Subscription)
