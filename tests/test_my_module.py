import pytest
from src.my_module import add, subtract
@pytest.fixture
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 2) == 0
    assert subtract(0, 1) == -1
