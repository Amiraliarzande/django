from django.shortcuts import render,get_object_or_404,HttpResponse
from blog.models import post , Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import Contactform, CommentForm
from django.contrib import messages


# Create your views here.

def blog_home(request,**kwargs):

    data = post.objects.filter(status=True,published_date__lte=timezone.now())

    if kwargs.get("cat_name") :
        data = data.filter(category__name=kwargs["cat_name"],published_date__lte=timezone.now())

    if kwargs.get("author_name") :
        data = data.filter(author__username=kwargs["author_name"],published_date__lte=timezone.now())

    if kwargs.get("tag_name") != None:
        data = data.filter(tags__name__in=[kwargs["tag_name"]],published_date__lte=timezone.now())

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
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The comment was submitted correctly.")
        else:
            messages.error(request, "The comment was not sent correctly.")

    posts = post.objects.filter(status=1)
    data = get_object_or_404(posts, id=pid)
    comment = Comment.objects.filter(post=data, approved=True)
    # استفاده از created_date مربوط به پست فعلی (data)
    previous_post = post.objects.filter(created_date__lt=data.created_date, status=1).order_by('-created_date').first()
    next_post = post.objects.filter(created_date__gt=data.created_date, status=1).order_by('created_date').first()

    context = {
        "post": data,
        "next_post": next_post,
        "previous_post": previous_post,
        "comments": comment,
    }
    return render(request, "blog/blog-single.html", context)

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


