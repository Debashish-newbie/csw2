from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from .models import Post


class PostURLTests(TestCase):
    def test_get_absolute_url_resolves_and_renders(self):
        user = get_user_model().objects.create_user(
            username="alice",
            email="alice@example.com",
            password="password123",
        )
        post = Post.objects.create(
            title="Hello",
            slug="hello",
            author=user,
            body="Body",
            status=Post.Status.PUBLISHED,
            publish=timezone.now(),
        )

        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
