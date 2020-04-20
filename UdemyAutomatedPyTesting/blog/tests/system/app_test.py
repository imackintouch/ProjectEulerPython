from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:  #Patch the built in print function
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_menu_prints_prompt(self):

        with patch('builtins.input') as mocked_input:  #Patch the built in input function
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
            # mocked_input.assert_called_with('Mama Mia')