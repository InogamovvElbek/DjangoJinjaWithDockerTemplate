from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse
from django.utils.timezone import localtime
from jinja2 import Environment


def environment(**options):
    """Django uchun Jinja2 muhiti: shablonlarda url(), static(), get_messages() va |localtime ishlaydi."""
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "get_messages": messages.get_messages,
        }
    )
    env.filters["localtime"] = localtime
    return env
