def is_palindrome(value) -> bool:
    s = str(value).lower()
    return s == s[::-1]


def test_is_palindrome_number_true():
    assert is_palindrome(121)

def test_is_palindrome_number_false():
    assert not is_palindrome(123)

def test_is_palindrome_word_true():
    assert is_palindrome("Level")

def test_is_palindrome_word_false():
    assert not is_palindrome("Python")
