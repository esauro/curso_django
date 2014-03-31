from django import template
from django.template.defaultfilters import title
from django.utils.safestring import mark_safe

register = template.Library()

def titlebold(value):
    value = title(value)
    return mark_safe("<strong>%s</strong>" % value)

register.filter("titlebold", titlebold)

def actions_menu(context, page):
    return {'page': page, 'post': context['post']}

register.inclusion_tag("blog/actions.html", takes_context=True)(actions_menu)