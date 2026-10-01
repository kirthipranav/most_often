from lib.most_often import *

def test_pytest():
    assert True

def test_empty_list():
    example = MostOften([])
    assert example.get_most_often() == "no clear winner"

def test_add_item():
    example = MostOften([])
    example.add_new(1)
    assert example.get_most_often() == 1