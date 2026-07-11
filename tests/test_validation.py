from post_handler import _validate_rq_body as validate_post


def test_rejects_non_dict():
    assert validate_post([1, 2]) is not None
    assert validate_post("hi") is not None
    assert validate_post(None) is not None


def test_rejects_missing_name():
    assert validate_post({"description": "x"}) is not None


def test_rejects_null_name():
    assert validate_post({"name": None, "description": "x"}) is not None


def test_rejects_missing_description():
    assert validate_post({"name": "x"}) is not None


def test_accepts_valid():
    assert validate_post({"name": "x", "description": "y"}) is None


def test_accepts_null_description():
    assert validate_post({"name": "x", "description": None}) is None
