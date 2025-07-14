from django import template
from blog.models import post , Category

register = template.Library()

@register.filter
def snippet (value,arg):
    return value[:arg] + "..."


@register.inclusion_tag("website/blog_latest.html")
def latest_blogs():
    posts = post.objects.filter(status=1).order_by("-published_date")[:6]
    return {"posts": posts}