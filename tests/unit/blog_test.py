from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Title', 'Allan')
        self.assertEqual('Title', blog.title)
        self.assertEqual('Allan', blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog = Blog('Title', 'Allan')
        another_blog = Blog('My day', 'Naomi')
        self.assertEqual(blog.__repr__(), 'Title by Allan (0 posts)')
        self.assertEqual(another_blog.__repr__(), 'My day by Naomi (0 posts)')

    def test_repr_multiple_posts(self):
        blog = Blog('Blog Title', 'Author')
        blog.posts = ['content']
        blog2 = Blog('Blog Title', 'Blog Author')
        blog2.posts = ['content', 'another_content']

        self.assertEqual(blog.__repr__(), 'Blog Title by Author (1 post)')
        self.assertEqual(blog2.__repr__(), 'Blog Title by Blog Author (2 posts)')
