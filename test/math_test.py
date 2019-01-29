from src import math_services as ms


def test_square_list():
    assert ms.square_list([]) == []
    assert ms.square_list([1]) == [1]
    assert ms.square_list([2]) == [4]
    assert ms.square_list([1, 2]) == [1, 4]
    assert ms.square_list([1, 2, 3]) == [1, 4, 9]
