import numpy as np
import pytest

from globagrim.trend import div_zonal_impulse, div_meridional_impulse, div_temperature_flow


@pytest.mark.parametrize(
    "div_func",
    [div_zonal_impulse, div_meridional_impulse, div_temperature_flow],
)
def test_divergence_functions_include_meridional_term(div_func):
    # Regression test: these functions used to silently drop the meridional
    # (v / dy) half of the divergence. A stray "+(...)" sitting on its own
    # line parsed as a no-op expression statement instead of being added to
    # the zonal term, so the result only ever reflected the zonal (u / dx)
    # part. Here u is all zero, so any nonzero result can only come from
    # the meridional term.
    NJ, NK, NL = 3, 3, 1
    shape = (NJ + 2, NK + 2, NL)
    u = np.zeros(shape)
    v = np.zeros(shape)
    weight = np.zeros(shape)
    cs = np.ones(NK + 2)
    dx = np.ones(NK + 2)
    dy = 1.0
    result = np.zeros(shape)

    v[2, 1, 0] = 2.0
    v[2, 2, 0] = 4.0
    v[2, 3, 0] = 6.0
    weight[2, 1, 0] = 1.0
    weight[2, 2, 0] = 1.0
    weight[2, 3, 0] = 1.0

    div_func(NK, NJ, result, u, weight, dx, v, cs, dy)

    assert result[2, 2, 0] == pytest.approx(2.0)
