def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.lower()) == sorted(s2.lower())


def test_are_anagrams_true():
    assert are_anagrams("listen", "silent")

def test_are_anagrams_false():
    assert not are_anagrams("hello", "world")

def test_are_anagrams_case_insensitive():
    assert are_anagrams("Tea", "Eat")

def test_are_anagrams_different_lengths():
    assert not are_anagrams("abc", "ab")
