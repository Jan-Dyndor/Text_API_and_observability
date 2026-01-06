import pytest
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker, declarative_base
from simple_text_api.config.conf import DATABASE_TEST_URL
from simple_text_api.main import app, get_db
from simple_text_api.db.models import (
    TextAnalysisResult,
)  # noqa

# We need to import this since import = running code, then SQLAlchemy sees the class that inherits from Base and adds info about this table to metadata. Without this import Base would not know whitch table to create
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


@pytest.fixture(scope="function")
def db_session():
    """Create new database and yield session"""
    engine_test = create_engine(
        DATABASE_TEST_URL, connect_args={"check_same_thread": False}
    )
    SessionLocalTest = sessionmaker(autoflush=False, autocommit=False, bind=engine_test)
    session = SessionLocalTest()
    Base.metadata.create_all(bind=engine_test)
    try:
        yield session
    finally:
        Base.metadata.drop_all(bind=engine_test)
        engine_test.dispose()
        session.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """
    Create test client and override FastAPI dependencies
    """

    def override_test_db():
        yield db_session

    app.dependency_overrides[get_db] = override_test_db

    with TestClient(app) as client:
        try:
            yield client
        finally:
            app.dependency_overrides.clear()
