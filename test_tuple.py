import pytest
from tuple_methods import t_size
from tuple_methods import t_count
from tuple_methods import t_pop

class TestTuple:

    def test_size(self):
        tt = tuple('hello')
        size = len(tt)
        assert t_size(tt) == size
    
    @pytest.mark.parametrize("test_input, excepted", [('h', 1), ('e', 1), ('l', 2), ('o', 1)])
    def test_count(self, test_input, excepted):
        tt = tuple('hello')
        assert t_count(tt, test_input) == excepted

    def test_pop(self):
        tt = tuple('hello')
        tt_new = tuple('hell')
        try:
            assert t_pop(tt) == tt_new
        except AttributeError:
            pass





