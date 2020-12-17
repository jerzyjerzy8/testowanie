from unittest.mock import MagicMock, patch
import pytest
from src.api import API, get_only_numbers


@pytest.fixture()
def my_mock():
    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]
    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    yield fake_api


def test_get_only_numbers(my_mock):
    expected = '1|4|5|25|23|4|324|24|1|23|545|32'
    with patch('src.api.API', my_mock):
        result = get_only_numbers()
        assert result == expected
