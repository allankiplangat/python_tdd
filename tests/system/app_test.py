from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Konza City', 'Allan')
        app.blogs = {'Konza City': blog}
        with patch('builtins.print') as mocked_print: # Context manager
            app.print_blogs()
            mocked_print.assert_called_with('- Konza City by Allan (0 posts)')
