from django import template
from django.template.defaultfilters import title
from django.utils.safestring import mark_safe

register = template.Library()

def titlebold(value):
    value = title(value)
    return mark_safe("<strong>%s</strong>" % value)

register.filter("titlebold", titlebold)