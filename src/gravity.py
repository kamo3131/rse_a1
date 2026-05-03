import pint
from numba import njit

si = pint.UnitRegistry()

@njit
def _calc_gravity(g_const, m1, m2, distance):
    return g_const * m1 * m2 / distance**2

def get_gravity(m1, m2, distance):
    m1_val = m1.to(si.kg).magnitude
    m2_val = m2.to(si.kg).magnitude
    d_val = distance.to(si.meter).magnitude
    G = si.Quantity(1, si.gravitational_constant).to_base_units().magnitude
    return _calc_gravity(G, m1_val, m2_val, d_val) * si.newton
