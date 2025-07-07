from django import template
from blog.models import post

register = template.Library()

@register.simple_tag
def status_post ():
    post_count = post.objects.filter(status=1).count()
    return post_count
    

@register.filter
def snippet (value,arg):
    return value[:arg] + "..."
