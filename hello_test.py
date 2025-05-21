import hello
import re

def test_hello():
    assert hello.hello_world() == "Hello, worlds!"

def test_lists_sum():
    l1 = [12, 34, 5435]
    l2 = [134, 1.444, 44]
    assert hello.list_sum(l1, l2) == 5660.444
