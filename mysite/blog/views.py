from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_list(request):
    try:
        posts = Post.publish.all()
    except Post.DoesNotExist:
        raise Http404("No Post found.")

    return render(request, "blog/post/list.xhtml", {"post": posts})


# Create your views here.
