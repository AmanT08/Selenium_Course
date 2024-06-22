# to run only one file from the folder
import pytest


# py.test filename.py -v -s

# to run only selective methods we use regular expression

# py.test -k string -v -s


@pytest.mark.smoke
def test_funSelected():
    print("selected in second file")


def test_fun2Selected():
    print("another one in second")


def test3_fun3():
    print("not selected in second")

@pytest.mark.smoke
def test_fun4Selected():
    print("running with mark")