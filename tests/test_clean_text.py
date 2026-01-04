from simple_text_api.services.clean_text import clean_input


def test_happy_input_clean(user_input_clean_text):
    clean_str = clean_input(user_input_clean_text)
    assert (
        clean_str
        == "data science data is powerful. machine learing will change the world."
    )


def test_dirty_input(dirty_user_input):
    clean_str = clean_input(dirty_user_input)
    assert clean_str == "data science is powerful"


def test_very_dirty_input(very_dirty_user_input):
    clean_str = clean_input(very_dirty_user_input)
    assert clean_str == "data science is powerful"


def test_dirty_input_many_sentences(dirty_user_input_many_sentences):
    clean_str = clean_input(dirty_user_input_many_sentences)
    assert (
        clean_str
        == "hello this is first sentence. second one and third sentence really."
    )
