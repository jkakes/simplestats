#stats.py
#This is a comment

def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals"""
    assert type(vals) is list, 'Input format is incorrect'
    total = sum(vals)
    length = len(vals)
    if length == 0:
    	return 0.0
    else:
    	return total/length


