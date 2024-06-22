# every pytest file name should start with test_ or end with _test

# every program should be wrapped in function

# cannot run like normal python files

# every method name should start with test_

import pytest


def test_fun():
    print("hello")


def test_fun2():
    print("world")



def test_fun3():
    print("python test")


@pytest.mark.smoke
def test_abcSelected():
    print("selected in first file")
