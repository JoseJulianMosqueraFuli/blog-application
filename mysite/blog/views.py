import os

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()


class PostListView(ListView):
    """
    Alternative post list view
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.xhtml"


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)  # Show 3 posts per page
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g. 9999),
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.xhtml", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.xhtml", {"post": post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(subject, message, os.getenv("EMAIL_HOST_USER"), [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, "blog/post/share.xhtml", {"post": post, "form": form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    new_comment = None
    form = CommentForm(data=request.Post)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request,
        "blog/post/comment.xhtml",
        {"post": post, "form": form, "comment": comment},
    )
