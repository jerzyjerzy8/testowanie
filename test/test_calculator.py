from src.calculator import add_numbers


def test_add_numbers_positive_numbers():
    a = 2
    b = 3
    result = 5
    assert add_numbers(a, b) == result


def test_add_numbers_negative_numbers():
    a = -2
    b = -3
    result = -5
    assert add_numbers(a, b) == result
