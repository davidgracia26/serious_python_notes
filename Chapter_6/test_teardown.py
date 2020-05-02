import pytest


@pytest.fixture(scope="module")
def database():
    db = 'connection string'
    yield db
    db.close()


def test_insert(database):
    database.insert(123)