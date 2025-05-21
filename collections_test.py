import collections

def test_lists_sum1():
    l1 = [12, 34, 5435]
    l2 = [134, 1.444, 44]
    assert collections.list_sum(l1, l2) == 5660.444
