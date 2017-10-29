import pytest

@pytest.fixture
def create_data():
    return 'We need that'

def test_needs(create_data):
    assert create_data == 'Do we need that?'