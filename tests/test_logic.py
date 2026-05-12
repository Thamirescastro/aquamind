import pytest
from src.logic import SelfCareManager

def test_add_water():
    sc = SelfCareManager()
    assert sc.add_water(500) == 500

def test_invalid_water():
    sc = SelfCareManager()
    with pytest.raises(ValueError):
        sc.add_water(-100)