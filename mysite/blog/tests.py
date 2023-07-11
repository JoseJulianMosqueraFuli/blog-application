from django.test import TestCase
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.models import User
from django.utils import timezone


class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )

        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.user,
            body="This is a test post",
            publish=timezone.now(),
            status=Post.Status.PUBLISHED,
        )

    def test_post_list_view(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/list.xhtml")

    def test_post_detail_view(self):
        response = self.client.get(
            reverse(
                "blog:post_detail",
                args=[
                    self.post.publish.year,
                    self.post.publish.month,
                    self.post.publish.day,
                    self.post.slug,
                ],
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/detail.xhtml")

    def test_post_share_view(self):
        response = self.client.get(reverse("blog:post_share", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/share.xhtml")

    def test_post_comment_view(self):
        response = self.client.post(
            reverse("blog:post_comment", args=[self.post.id]),
            data={
                "name": "Test User",
                "email": "test@example.com",
                "body": "This is a test comment",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/comment.xhtml")
        self.assertContains(response, "Test User")
        self.assertContains(response, "This is a test comment")

    def test_comment_model(self):
        comment = Comment.objects.create(
            post=self.post,
            name="Test User",
            email="test@example.com",
            body="This is a test comment",
        )
        self.assertEqual(str(comment), f"Comment by {comment.name} on {comment.post}")
