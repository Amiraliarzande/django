from django import template
from blog.models import post
from blog.models import post , Category

register = template.Library()

@register.simple_tag
def status_post ():
    post_count = post.objects.filter(status=1).count()
    return post_count
    

@register.filter
def snippet (value,arg):
    return value[:arg] + "..."


@register.inclusion_tag("popularposts.html")
def inclusion ():
    posts = post.objects.filter(status=1).order_by("updated_date")
@register.inclusion_tag("blog/recentposts.html")
def popular ():
    posts = post.objects.filter(status=1).order_by("published_date")[:3]
    return {"posts":posts}
@register.inclusion_tag("blog/category_display.html")
def category_display ():
    posts = post.objects.filter(status=1)
    categorys = Category.objects.all()
    cat_dict = {}
    for name in categorys :
        cat_dict[name] = posts.filter(category=name).count
    return {"category" : cat_dict}