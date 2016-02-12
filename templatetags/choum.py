from django import template

register = template.Library()

@register.filter(name='setval')
def setval(value, arg):
    value = arg
    return value