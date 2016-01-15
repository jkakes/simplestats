#stats.py
#This is a comment

def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals"""
    assert type(vals) is list, 'Input format is incorrect'
    total = sum(vals)
    length = len(vals)
    return total/length


def test_mean():
    assert mean([2,4]) == 3.0, 'Simple mean test'

 test_mean()

 def test_empty_list():
    assert mean([]) is None, 'Empty list test'```