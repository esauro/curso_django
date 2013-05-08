from django.test import TestCase
from models import Post


class SimpleTest(TestCase):
    fixtures = ['posts.json']

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_post(self):
        p = Post.objects.get(pk = 1)
        self.assertEqual("Post1", p.title)
