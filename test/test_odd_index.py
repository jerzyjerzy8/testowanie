from src.odd_index import odd_index
import pytest


@pytest.mark.parametrize('napis, result', [('teleturniej', 'eeune'),
                                           ('komputer', 'optr'),
                                           (1234, '24')])
def test_odd_index_parametrized(napis, result):
    assert odd_index(napis) == result


'''
def test_odd_index_one():
    assert odd_index('teleturniej') == 'eeune'


def test_odd_index_two():
    assert odd_index('komputer') == 'optr'


def test_odd_index_number():
    assert odd_index(1234) == '24'
'''