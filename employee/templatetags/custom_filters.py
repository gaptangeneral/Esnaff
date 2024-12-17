from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    try:
        return field.as_widget(attrs={'class': css_class})
    except AttributeError:
        # field bir form alanı değilse, olduğu gibi döndür
        return field