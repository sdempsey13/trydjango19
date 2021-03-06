from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_athenticated():
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def posts_list(request):
        queryset_list = Post.objects.all()
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
            ).distinct()
        paginator = Paginator(queryset_list, 2) # Show 5 contacts per page
        page = request.GET.get('page')
        queryset_list = paginator.get_page(page)
        context = {
            "object_list": queryset_list,
            "title": "List of Blogs",
        }
        return render(request, "post_list.html", context)




def posts_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def posts_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return render(request, "base.html")
