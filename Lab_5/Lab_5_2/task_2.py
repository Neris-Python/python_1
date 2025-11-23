def find_unique(lst: list) -> list:
    return [x for x in lst if lst.count(x) == 1]


def test_find_unique_empty():
    assert find_unique([]) == []

def test_find_unique_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_find_unique_with_duplicates():
    assert find_unique([1, 2, 2, 3, 3, 4]) == [1, 4]

def test_find_unique_strings():
    assert find_unique(["a", "b", "a", "c"]) == ["b", "c"]
