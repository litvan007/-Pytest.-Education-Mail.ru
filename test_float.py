import pytest
import math
from float_methods import f_pi
from float_methods import f_pi
from float_methods import f_pop

class TestTuple:

    def test_pi(self):
        try:
            assert f_pi() == math.pi
        except False:
            pass
    
    @pytest.mark.parametrize("test_input, excepted", [('float(10*2)', 20)])
    def test_multiply(self, test_input, excepted):
        assert f_multiply(test_input) == excepted

    def test_eq(self):
        a = 1
        b = 1
        assert f_eq(a, b) == True 
