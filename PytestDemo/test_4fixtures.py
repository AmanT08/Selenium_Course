# FIXTURES IN PYTEST
# WE DEFINE A METHOD AS FIXTURE WHEN WE WANT TO USE IT AGAIN AND AGAIN
# LIKE PASSING URL, OR TAKING INPUTS WHICH WILL BE REQUIRED BY
# OTHER METHODS OF THE PROGRAM

import pytest


@pytest.fixture()
def input_by_user():
    a=20
    return a


def test_first_method(input_by_user):
    b=20
    b= b+input_by_user
    print(b)


def test_second_method(input_by_user):
    c=20
    c=c- input_by_user
    print(c)




