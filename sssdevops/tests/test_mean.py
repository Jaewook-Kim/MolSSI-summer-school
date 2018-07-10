"""
This file is to test the mean function
"""
from sssdevops import mean
import pytest


def test_simple():
    num_list = [1, 2]
    observed = mean(num_list)
    expected = 1.5
    assert observed == expected   # assert : test boolean expression. If true, do nothing 

@pytest.fixture   # tell pytest "if num_list variable is called, use this new one!"
def num_list():   # same name as argument! everytime it gives freshly made variable.
    return [1, 2, 3, 4, 5]

@pytest.mark.skip("I want to skep")
def test_more(num_list):
    assert mean(num_list) == 3.0

def test_empty():
    with pytest.raises(ZeroDivisionError):  #len(list)==0 ZeroDivisionError, if not, give error
        mean([])

@pytest.mark.parametrize("num_list", [
    ("this is string"),
    ([1,'1','a']),
    (3)])
def test_type_error(num_list):
    with pytest.raises(TypeError):
        mean(num_list)

#python decorator
@pytest.mark.parametrize("num_list, expected_mean", [
    ([1, 2, 3, 4, 5], 3.0),
    ([1, 2], 1.5),
    ([1], 1.0),
    ([-1, 0, 2, 0],0.25),
    ([3.7, 2.3], 3.0),
])    #parameterize(arg_list as string, list of tuple)
def test_many(num_list, expected_mean):     #We should do assert a==b every time..  So We can parametrize it.
    assert mean(num_list) == expected_mean
