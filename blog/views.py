from django.shortcuts import render,get_object_or_404
from .models import post

# Create your views here.

def blog_home(request):

    data = post.objects.all()
    context = {
        "posts": data,
    }

    return render(request, "blog/blog-home.html",context)

def blog_single(request):
    context = {
        "name" : "ashkan",
        "last_name" : "arzandeh",
    }
    return render(request, "blog/blog-single.html",context)

def test(request,pk):

    data = get_object_or_404(post,id=pk)
    context = {
        "posts": data,
    }

    return render(request, "test.html", context)