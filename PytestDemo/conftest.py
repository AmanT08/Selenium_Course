# in the conftest file we write all the fixtures that are common
# in every program
# compiler will check this file when it sees the name of a fixture in program file
# THE NAME OF THIS FILE SHOULDN'T BE CHANGED

import pytest


@pytest.fixture(scope="class")
def Browser_Method():
    # like invoking browser or something
    print("before the methods")


@pytest.fixture()
def data_load():
    list1 = ["Aman", "Thapliyal", 24]
    return list1


@pytest.fixture(params=(("aman","thapliyal"),("ramesh","abc"),("suresh","def")))
def parameterize(request):
    return request.param


