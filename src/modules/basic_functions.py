from flask import jsonify


def to_json(python_obj):
    """
    Converts a Python object to JSON.

    Receives
    --------
    python_obj : list, numpy.array, integer, double, etc.
        Any Python object.

    Returns
    -------
    json_object : JSON
        Converted JSON object.
    """

    return jsonify(python_obj)
