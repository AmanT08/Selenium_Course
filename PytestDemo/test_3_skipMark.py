# to skip few test cases while running all
import pytest


# we mark them with skip

# @pytest.mark.skip

# skip is predifined marking name

def test_funn():
    print("not skipped")


@pytest.mark.xfail
def test_funnnn2():
    print("hello")
    b = 2/0
    print(b)
    print("skipped so wont get printed")