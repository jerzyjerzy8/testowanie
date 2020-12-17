from src.warehouse import Product, Warehouse
import pytest


@pytest.fixture()
def data_1():
    wh = Warehouse(10)
    pl = [Product('cola', 2.24), Product('konserwa', 4.44), Product('mąka', 3.00)]
    yield wh, pl


@pytest.fixture()
def data_2():
    wh = Warehouse(2)
    pl = [Product('cola', 0.88), Product('konserwa', 1.05), Product('mąka', 0.50)]
    yield wh, pl


def test_warehouse_with_products_list_1(data_1):
    wh, pl = data_1
    for p in pl:
        assert wh.add(p) is None
    assert wh.get_current_stock() == 9.68


def test_warehouse_with_products_list_2(data_2):
    wh, pl = data_2
    assert wh.add(pl[0]) is None
    assert wh.add(pl[1]) is None
    assert wh.add(pl[2]) == -1
    assert wh.get_current_stock() == 1.93
