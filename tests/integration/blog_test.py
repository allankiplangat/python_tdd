from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test Title', 'Author')
        b.create_post("Kenya", "Amazing Kenya")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Kenya')
        self.assertEqual(b.posts[0].content, "Amazing Kenya")

    def test_json_no_posts(self):
        b = Blog('Test Title', 'Author')
        expected = {'title': 'Test Title', 'author': 'Author', 'posts': []}
        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test Title', 'Author')
        b.create_post("Kenya", "Amazing Kenya")

        expected = {
            'title': 'Test Title',
            'author': 'Author',
            'posts': [
                {'title': "Kenya",
                 'content': 'Amazing Kenya'}
            ]
        }
        self.assertDictEqual(expected, b.json())
