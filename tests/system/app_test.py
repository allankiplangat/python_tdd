from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Konza City', 'Allan')
        app.blogs = {'Konza City': blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')

                app.menu()

                mocked_ask_create_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print: # Context manager
            app.print_blogs()
            mocked_print.assert_called_with('- Konza City by Allan (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value = 'Konza City'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Konza City'])

    def test_print_posts(self):
        blog = app.blogs['Konza City']
        blog.create_post('Test Post', 'Test Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Title', 'Content')
        expected_print = '''
--- Title ---

Content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Konza City', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Konza City'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Konza City'].posts[0].content, 'Test Content')
















