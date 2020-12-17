from src.avg import get_avg
from unittest.mock import MagicMock, patch


def test_get_avg():
    mock = MagicMock()
    mock.return_value = '76313'
    with patch('src.avg.get_data', mock):
        assert get_avg('whatever') == 4
