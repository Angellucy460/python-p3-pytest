# lib/testing/test_not_none.py
from not_none_functions import get_name

def test_get_name_is_not_none():
    assert get_name() is not None