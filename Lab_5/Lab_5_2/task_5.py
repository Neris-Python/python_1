def combine_dicts(d1: dict, d2: dict) -> dict:
    result = {}
    result.update(d1)
    result.update(d2)
    return result


def test_combine_dicts_empty():
    assert combine_dicts({}, {}) == {}

def test_combine_dicts_first_non_empty():
    assert combine_dicts({"a": 1}, {}) == {"a": 1}

def test_combine_dicts_second_overwrites_first():
    assert combine_dicts({"a": 1}, {"a": 2}) == {"a": 2}

def test_combine_dicts_merge():
    assert combine_dicts({"a": 1, "b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}
