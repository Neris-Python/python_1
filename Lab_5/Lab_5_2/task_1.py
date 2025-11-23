def count_words(sentence: str) -> int:
    if not sentence.strip():
        return 0
    return len(sentence.split())


def test_count_words_empty():
    assert count_words("") == 0

def test_count_words_single():
    assert count_words("Hello") == 1

def test_count_words_multiple():
    assert count_words("Hello world from pytest") == 4

def test_count_words_spaces():
    assert count_words("   Hello   world   ") == 2
