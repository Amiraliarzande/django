from django.shortcuts import render
from .models import post

# Create your views here.

def blog_home(request):
    return render(request, "blog/blog-home.html")

def blog_single(request):
    context = {
        "name" : "ashkan",
        "last_name" : "arzandeh",
    }
    return render(request, "blog/blog-single.html",context)

def test(request):

    deta = post.objects.all()
    context = {
        "posts": deta,
    }

    return render(request, "test.html", context)