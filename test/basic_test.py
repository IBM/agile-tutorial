from src import basic_services as bs


def test_csv_to_list():
    assert bs.csv_to_list('1') == [1]
    assert bs.csv_to_list('1,2') == [1, 2]
    assert bs.csv_to_list('1,2,3') == [1, 2, 3]
