import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from simple_text_api.config.conf import DATABASE_TEST_URL

from simple_text_api.db.models import (
    TextAnalysisResult,
)  # noqa need for table creation. To Base to create table we need to have imported models of the tables
from simple_text_api.db.database import (
    Base,
)  # Important ! We need to use the same BASE as in production database since our db model inherits from it and knows the models


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


engine_test = create_engine(
    DATABASE_TEST_URL, connect_args={"check_same_thread": False}
)

SessionLocalTest = sessionmaker(autoflush=False, autocommit=False, bind=engine_test)

Base.metadata.create_all(bind=engine_test)


def get_test_db():
    db_test = SessionLocalTest()
    try:
        yield db_test
    finally:
        db_test.close()
