#test_stats.py

from stats import mean
from nose.tools import assert_equal


def test_mean():
    assert_equal(mean([2,4]),3.0)
#test_mean()

def test_empty_list():
    assert_equal(mean([]),0.0)
#test_empty_list()

def test_float():
	assert_equal(mean([3,4]),3.5)
#test_float()