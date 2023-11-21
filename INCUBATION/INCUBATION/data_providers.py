import pytest

@pytest.mark.parametrize("param1, param2", [(1,4), (2,8), (3,12)])
def test_calc(param1,param2):
    assert param2 == 4*param1