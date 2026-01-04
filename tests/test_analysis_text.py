from simple_text_api.services.text_analysis import (
    count_sentences,
    count_words,
    most_frequent_char,
    most_frequent_words,
)


def test_text_analysis_word_count(user_input_clean_text):
    words_count: int = count_words(user_input_clean_text)
    assert words_count == 11


def test_text_analysis_count_sentences(user_input_clean_text):
    sentences: int = count_sentences(user_input_clean_text)
    assert sentences == 2


def test_text_analysis_frequent_chars(user_input_clean_text):
    chars_dict: dict = most_frequent_char(user_input_clean_text)
    assert chars_dict[" "] == 10
    assert chars_dict["a"] == 7
    assert chars_dict["e"] == 7
    assert chars_dict["i"] == 5
    assert chars_dict["l"] == 5
    assert chars_dict["c"] == 4
    assert chars_dict["n"] == 4
    assert chars_dict["d"] == 3
    assert chars_dict["t"] == 3
    assert chars_dict["w"] == 3
    assert chars_dict["r"] == 3


def test_text_analysis_frequent_words(user_input_clean_text):
    words: dict = most_frequent_words(user_input_clean_text)
    assert words["data"] == 2
    assert words["science"] == 1
    assert words["powerful"] == 1
    assert words["machine"] == 1
    assert words["learing"] == 1
    assert words["change"] == 1
    assert words["world"] == 1
