from src import math_services as ms


def test_product():
    assert ms.product([1]) == 1.0
    assert ms.product([2]) == 2.0
    assert ms.product([1, 1]) == 1.0
    assert ms.product([1, 2]) == 2.0
    assert ms.product([1, 2, 3]) == 6.0
    assert ms.product([0, 1, 2, 2]) == 0.0
    assert ms.product([1, 1, 2, 3]) == 6.0
    assert ms.product([1, 2, 4, 5]) == 40.0
    assert ms.product([1, 2, 3, 4, 5]) == 120.0


def test_square_list():
    assert ms.square_list([]) == []
    assert ms.square_list([1]) == [1]
    assert ms.square_list([2]) == [4]
    assert ms.square_list([1, 2]) == [1, 4]
    assert ms.square_list([1, 2, 3]) == [1, 4, 9]
