from django import template

register = template.Library()

from icecream import ic


@register.simple_tag(takes_context=True)
def delete_session_variable(context, variable_name):
    request = context["request"]
    if variable_name in request.session:
        del request.session[variable_name]
    return ""
