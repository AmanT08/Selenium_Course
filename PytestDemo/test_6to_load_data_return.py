# just pass the fixture name as argument in the method

import pytest

@pytest.mark.usefixtures("data_load")
class Test_load_data:
    def test_user_value(self,data_load):
        print(data_load[0])
        print(data_load[2])


def test_param(parameterize):
    print(parameterize[1])

