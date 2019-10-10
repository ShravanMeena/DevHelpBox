from django import template

register = template.Library()

@register.filter(name='update_ano')
def update_ano(value):
    ano = value
    return ano
