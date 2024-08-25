from django import template

register = template.Library()

@register.filter(name='price_form')
def price_form(value):
    if value is None:
        return ''
    return "{:,.1f}".format(value).replace(",", " ").replace('.',',')
