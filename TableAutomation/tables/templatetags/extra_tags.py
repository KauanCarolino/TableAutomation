from django import template
from django.db.models import Model

register = template.Library()

@register.filter
def get_attr(value, arg):
    if isinstance(value, Model):
        return getattr(value, arg, '')
    return ''
