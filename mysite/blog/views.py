from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.publish.all()
    return render(request, "blog/post/list.xhtml", {"post": posts})


# Create your views here.
