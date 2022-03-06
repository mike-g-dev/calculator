from calculator.calculator import add, subtract
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2], 3),
    ([1, 0], 1),
    ([0, 1], 1),
    ([-1, 1], 0),
    ([100, 300], 400)
])
def test_add(test_input, expected):
    assert add(*test_input) == expected


def test_symmetry():
    assert add(1, 2) == add(2, 1)


def test_subtract():
    assert subtract(10, 6) == 4
