from django import template

from djfavicon.utils import get_favicon


register = template.Library()


@register.filter
def favicon(url):
    """
    render favicon related to url using Google favicon service
    """
    return get_favicon(url)
    
    