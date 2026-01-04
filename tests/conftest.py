import pytest


@pytest.fixture
def user_input_clean_text() -> str:
    return "data science data is powerful. machine learing will change the world."


@pytest.fixture
def dirty_user_input() -> str:
    return "  Data,   Science! Is  Powerful?  "


@pytest.fixture
def very_dirty_user_input() -> str:
    return "\n@Data!!!  sciEnce??\t is () powerful [] {}\n"


@pytest.fixture
def dirty_user_input_many_sentences() -> str:
    return "Hello!!!  This is first sentence.\n\nSecond one??  And third: sentence! @Really."
