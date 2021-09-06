from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm


def subscriber_form_context(request):
    """
    Newsletter input validation
    and context provider.
    """
    if request.method == 'POST':
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            instance = subscriber_form.save(commit=False)
            if Subscriber.objects.filter(
                    user_email=instance.user_email).exists():
                messages.error(request,
                               'Sorry, the email already exists in our list')
            else:
                subscriber_form.save()
                subscriber_form = SubscriberForm()
                messages.success(request,
                                 'Thank youfor subscribing \
                                        to our newsletter')
    else:
        subscriber_form = SubscriberForm()

    context = {
        'subscriber_form': subscriber_form,
        }

    return context