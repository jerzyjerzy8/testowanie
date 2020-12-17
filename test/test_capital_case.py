import pytest
from src.capital_case import capital_case


def test_regular_phrase():
    assert capital_case('ala ma kota') == 'Ala ma kota'


def test_number():
    with pytest.raises(TypeError):
        capital_case(123)
