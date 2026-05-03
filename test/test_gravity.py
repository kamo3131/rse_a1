import pytest
from gravity import get_gravity, si

def test_answer():
    assert get_gravity(5.97e24*si.kg, 1*si.kg, 6371*si.km).magnitude == pytest.approx(9.8, rel=1e-2)
