# custom templates

from django import template

#GEt instance of template.Library
register = template.Library()

#define operation
def cut(value,arg):
    """
    This cuts all values of arg from the string!
    """
    return value.replace(arg,'')

#register the operation Function
register.filter('cut',cut)

#registering filters using decorators
@register.filter(name='add_placeholder')
def add_placeholder(value,arg):
    value.field.widget.attrs.update({'placeholder':arg})
    return value

@register.filter(name='add_class')
def add_class(value,arg):
    value.field.widget.attrs.update({'class':arg})
    return value
