#test_stats.py

from stats import mean

def test_mean():
    assert mean([2,4]) == 3.0, 'Simple mean test'
test_mean()

def test_empty_list():
    assert mean([]) == 0.0
test_empty_list()

def test_float
	assert mean([3,4]) == 3.5
test_float()