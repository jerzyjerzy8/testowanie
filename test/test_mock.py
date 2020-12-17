from unittest.mock import MagicMock
from src.mock import User
import pytest


@pytest.fixture()
def user():
    account_1 = MagicMock()
    account_1.get_balance.return_value = 50
    account_2 = MagicMock()
    account_2.get_balance.return_value = 40
    user = User('Kowalski', 35, [account_1, account_2])
    yield user


def test_return_available_funds(user):
    assert user.get_available_funds() == 90
