from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        post = Post('Test Title', 'Test Content')
        self.assertEqual('Test Title', post.title)
        self.assertEqual('Test Content', post.content)

    def test_json(self):
        post = Post('Test Title', 'Test Content')
        expected = {'title': 'Test Title', 'content': 'Test Content'}
        self.assertDictEqual(expected, post.json())



