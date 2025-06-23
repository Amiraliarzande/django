from django.shortcuts import render,get_object_or_404
from .models import post
from django.utils import timezone

# Create your views here.

def blog_home(request):

    data = post.objects.filter(status=True,published_date__lte=timezone.now())
    context = {
        "posts": data,
    }

    return render(request, "blog/blog-home.html",context)

def blog_single(request):
def blog_single(request,pid):
    posts = post.objects.filter(status=1)
    data = get_object_or_404(posts, id=pid)
    context = {
        "name" : "ashkan",
        "last_name" : "arzandeh",
        "post" : data
    }
    return render(request, "blog/blog-single.html",context)

def test(request,pk):

    data = get_object_or_404(post,id=pk)
    context = {
        "posts": data,
    }

    return render(request, "test.html", context)