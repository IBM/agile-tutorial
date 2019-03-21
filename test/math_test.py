from src import math_services as ms


def test_double_list():
    assert ms.double_list([]) == []
    assert ms.double_list([1]) == [2]
    assert ms.double_list([2]) == [4]
    assert ms.double_list([1, 2]) == [2, 4]
    assert ms.double_list([1, 2, 3]) == [2, 4, 6]
