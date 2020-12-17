from src.sum_args import sum_args


def test_sum_of_elements_below_max_value():
    max_value = 10
    elements = [2, 4, 5, 3, 9, 1, 0, -2]
    result = 22
    assert sum_args(max_value, elements) == result


def test_sum_of_elements_above_max_value():
    max_value = 8
    elements = [2, 4, 5, 3, 9, 1, 0, -2]
    result = 13
    assert sum_args(max_value, elements) == result


def test_sum_of_elements_with_string():
    max_value = 8
    elements = [2, 4, 5, 3, 'Ala']
    result = 14
    assert sum_args(max_value, elements) == result


def test_sum_of_elements_with_string_max_value():
    max_value = 'Ala'
    elements = [2, 4, 5, 3]
    result = 14
    assert sum_args(max_value, elements) == result


def test_sum_of_elements_with_string_all():
    max_value = 'Ala'
    elements = [2, 4, 5, 3, 'Ala']
    result = 14
    assert sum_args(max_value, elements) == result
