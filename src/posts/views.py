from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def posts_create(request):
    return HttpResponse("<h1>Hello World!</h1>")

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def posts_list(request):
        queryset = Post.objects.all()
        context = {
            "object_list": queryset,
            "title": "List",
        }
        return render(request, "index.html", context)

def posts_update(request):
    return HttpResponse("<h1>Hello World$</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Hello World%</h1>")
