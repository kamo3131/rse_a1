import pint
from numba import njit

si = pint.UnitRegistry()
G_CONST = 6.67430e-11
@njit
def _calc_gravity(g_const, m1, m2, distance):
    """Returns the value of gravity without pint units."""
    return g_const * m1 * m2 / distance**2

def get_gravity(m1, m2, distance):
    """Returns gravity value with Units."""
    m1_val = m1.to(si.kg).magnitude
    m2_val = m2.to(si.kg).magnitude
    d_val = distance.to(si.meter).magnitude
    return _calc_gravity(G_CONST, m1_val, m2_val, d_val) * si.newton
