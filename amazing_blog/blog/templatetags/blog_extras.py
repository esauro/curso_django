from django import template
from django.template.defaultfilters import title
from django.utils.safestring import mark_safe

register = template.Library()

def titlebold(value):
    value = title(value)
    return mark_safe("<strong>%s</strong>" % value)

register.filter("titlebold", titlebold)

def actions_menu(context, page):
    out_context = {'page': page}
    if context.has_key("post"):
        out_context['post'] = context['post']
    return out_context

register.inclusion_tag("blog/actions.html", takes_context=True)(actions_menu)