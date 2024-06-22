# here we make simple use of fixture and then in class

#  CLASS NAME STARTS WITH TEST

import pytest


@pytest.mark.usefixtures("Browser_Method")
class TestFixtureExample:

    def test_hello(self):
        print("hello")

    def test_method1(self):
        print("class and method 1")

    def test_method2(self):
        print("class and method 2")

    def test_method3(self):
        print("class and method 3")

    def test_method4(self):
        print("class and method 4")
