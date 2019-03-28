from src import math_services as ms


def test_double_list():
    assert ms.double_list([]) == []
    assert ms.double_list([1]) == [2]
    assert ms.double_list([2]) == [4]
    assert ms.double_list([1, 2]) == [2, 4]
    assert ms.double_list([1, 2, 3]) == [2, 4, 6]


def test_mean():
    assert ms.mean([1]) == 1.0
    assert ms.mean([2]) == 2.0
    assert ms.mean([1, 1]) == 1.0
    assert ms.mean([1, 2]) == 1.5
    assert ms.mean([1, 2, 3]) == 2.0
    assert ms.mean([0, 1, 2, 2]) == 1.25
    assert ms.mean([1, 1, 2, 3]) == 1.75
    assert ms.mean([1, 2, 4, 5]) == 3.0
    assert ms.mean([1, 2, 3, 4, 5]) == 3.0


def test_square_list():
    assert ms.square_list([]) == []
    assert ms.square_list([1]) == [1]
    assert ms.square_list([2]) == [4]
    assert ms.square_list([1, 2]) == [1, 4]
    assert ms.square_list([1, 2, 3]) == [1, 4, 9]


def test_triple_list():
    assert ms.triple_list([]) == []
    assert ms.triple_list([1]) == [3]
    assert ms.triple_list([2]) == [6]
    assert ms.triple_list([1, 2]) == [3, 6]
    assert ms.triple_list([1, 2, 3]) == [3, 6, 9]
