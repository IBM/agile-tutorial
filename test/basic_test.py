from src import basic_services as bs


def test_csv_to_list():
    assert bs.csv_to_list('1') == [1]
    assert bs.csv_to_list('1,2') == [1, 2]
    assert bs.csv_to_list('1,2,3') == [1, 2, 3]


def test_unique():
    assert bs.unique([]) == []
    assert bs.unique([1]) == [1]
    assert bs.unique([1, 1]) == [1]
    assert bs.unique([1, 1, 1]) == [1]
    assert bs.unique([1, 2, 1]) == [1, 2]
    assert bs.unique([1, 2, 3]) == [1, 2, 3]
    assert bs.unique([1, 2, 3, 1]) == [1, 2, 3]
    assert bs.unique([1, 2, 3, 1, 2]) == [1, 2, 3]
    assert bs.unique([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
