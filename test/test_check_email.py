import pytest
from src.check_email import check_email_format


def test_check_email_format_good():
    result = 'Email format OK'
    assert check_email_format('mojemail@gmail.com') == result


def test_check_email_format_bad():
    with pytest.raises(Exception):
        assert check_email_format('asdasd.com')
