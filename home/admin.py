from django.contrib import admin
from .models import Newsletter


class Email_Subscription(admin.ModelAdmin):
    fields = (
        'user_email',
        'subscribed',
    )

    list_display = (
        'user_email',
        'subscribed',)


admin.site.register(Newsletter, Email_Subscription)
