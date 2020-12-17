from unittest.mock import MagicMock, patch
from src.blog import BlogPostHistory
import pytest


def test_change_title():
    mock = MagicMock()
    with patch('src.blog.BlogPostHistory.save', mock):
        post_history = BlogPostHistory('Ala', 'Ala ma kota')
        post_history.change_title('Kasia')
        assert post_history.get_properties() == ('Kasia', 'Ala ma kota')


def test_problem_with_file():
    mock = MagicMock(side_effect=OSError)
    with patch('src.blog.BlogPostHistory.save', mock):
        post_history = BlogPostHistory('Ala', 'Ala ma kota')
        with pytest.raises(Exception):
            post_history.change_title('Kasia')
