from django.shortcuts import render,get_object_or_404
from .models import post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog_home(request,**kwargs):

    data = post.objects.filter(status=True,published_date__lte=timezone.now())

    if kwargs.get("cat_name") :
        data = data.filter(category__name=kwargs["cat_name"],published_date__lte=timezone.now())

    if kwargs.get("author_name") :
        data = data.filter(author__username=kwargs["author_name"],published_date__lte=timezone.now())

    p = Paginator(data , 3)
    page_number  = request.GET.get('page')
    try : 
        data = p.get_page(page_number)
    except PageNotAnInteger :
        data = p.get_page(1)
    except EmptyPage :
        data = p.get_page(p.num_pages)

    context = {
        "posts": data,
    }

    return render(request, "blog/blog-home.html",context)


def blog_single(request, pid):
    posts = post.objects.filter(status=1)
    data = get_object_or_404(posts, id=pid)

    # استفاده از created_date مربوط به پست فعلی (data)
    previous_post = post.objects.filter(created_date__lt=data.created_date, status=1).order_by('-created_date').first()
    next_post = post.objects.filter(created_date__gt=data.created_date, status=1).order_by('created_date').first()

    context = {
        "post": data,
        "next_post": next_post,
        "previous_post": previous_post
    }
    return render(request, "blog/blog-single.html", context)

def test(request,pk):

    data = get_object_or_404(post,id=pk)
    context = {
        "posts": data,
    }

    return render(request, "test.html", context)


def blog_search(request):
    data = post.objects.filter(status=True,published_date__lte=timezone.now())

    if request.method == "GET" :
        query = request.GET.get("q")
        if query:
            data = data.filter(content__icontains=query)

    context = {
        "posts": data,
    }

    return render(request, "blog/blog-home.html",context)