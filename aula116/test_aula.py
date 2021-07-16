import pytest

def soma_1(n):
    return int(n) + 1

def test_soma_1():
    assert soma_1(41) == 42

def teste_soma_1_como_string():
    assert soma_1("41") == 42

def test_soma_1_palavra():
    with pytest.raises(ValueError):
        assert soma_1("fabio") == 0