from django import template 

register = template.Library()


def get_item(dictionary, key):
    """Access a dictionary by key in a template."""
    return dictionary.get(key)


register.filter('get_item',get_item)