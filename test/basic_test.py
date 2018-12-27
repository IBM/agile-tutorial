from main import app
from src import basic_functions as bf


def test_to_json():
    with app.app_context():
        assert bf.to_json(0).data == b'0\n'
        assert bf.to_json([]).data == b'[]\n'
        assert bf.to_json([1]).data == b'[1]\n'
        assert bf.to_json([1, 2]).data == b'[1,2]\n'
