import pytest


@pytest.fixture
def before_after():

    yield None


def test_1(before_after):
    assert 1 == 1

def test_2(before_after):
    assert 2 == 2, "ОшибОчка"
