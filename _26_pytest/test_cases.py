from turtle import end_fill
from _1_pytest_demo import fun

def test_add_int():
    assert fun(3,1) == 4, "the value didn't match!"

def test_add_str():
    assert fun("a","b") == "abc"

class TestSample:
    def test_add_int(self):
        assert fun(3,1) == 4

    def test_add_str(self):
        assert fun("a","b") == "ab"

