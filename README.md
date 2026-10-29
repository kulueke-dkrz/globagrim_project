
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcoKulueke/globagrim_project/HEAD)

# Global Atmospheric Grid Point Model

![logo](https://github.com/MarcoKulueke/globagrim_project/blob/main/png/logo.png?raw=true)

GLOBAGRIM is a simplified global atmospheric circulation model: it solves the
primitive equations on a latitude/longitude grid with sigma vertical
coordinates, stepping surface pressure, wind, and temperature forward in time
from a chosen initial condition. It's meant as a compact, readable
illustration of how a grid-point atmospheric model works, not an
operational forecast model.

It is inspired by GLOBAGIM of CLISAP (more information can be found via: https://www.clisap.de/research/b:-climate-manifestations-and-impacts/crg-dynamical-systems/models/globagim/).

## Installation
Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then from the repository root run:
```bash
uv sync
```
This creates a `.venv` with GLOBAGRIM and all dependencies installed, pinned exactly per `uv.lock`.
Then, run commands inside the environment with `uv run`, e.g.:
```bash
uv run python
```
or activate it directly with:
```bash
source .venv/bin/activate
```
To also install the development/docs extras (`jupyter`, `pytest`, `sphinx`), run `uv sync --extra dev` instead.

---
### Alternative
If you already have `numpy`, `xarray`, `netcdf4`, `matplotlib`, `cartopy`, `numba`, `pip` installed, you could add the GLOBAGRIM package to your current environment by executing:
```bash
pip install git+https://github.com/MarcoKulueke/globagrim_project.git#egg=globagrim
```
---

## Example Usage

A minimal end-to-end example - run the model, then plot a field from the result:

```python
from globagrim import model

model.run()
model.plot()
```

### Running the model

```python
model.run()
```

All parameters are optional and keyword-only; any you omit keep their
previous value (the first call uses the built-in defaults). `model.run()`
writes its output to a NetCDF file at `OUT` as it integrates:

- `NJ` Number of west-east circles of longitude
- `NK` Number of north-south circles of latitude
- `NL` Number of vertical levels
- `TF` Total integration time, in hours
- `DT` Integration time step, in seconds
- `IEXP` Experiment number, selecting the initial condition:
  - `1` - low pressure system over the Pacific
  - `2` - flow over an isolated mountain in North America
  - `3` - random wind field
- `INT` Output interval in hours (`0`, the default, writes every time step)
- `OUT` Output NetCDF file path

### Visualizing the results

```python
model.plot()
```

Reads back the NetCDF file written by the preceding `model.run()` call and
renders one field as a map, so `model.run()` must be called at least once
before `model.plot()`. All parameters are optional:

- `var_name` Field to plot - one of:
  - `SE` Surface elevation (orography)
  - `PSG` Sea level pressure
  - `T` Temperature
  - `U` Zonal (east-west) wind
  - `V` Meridional (north-south) wind
- `out_step` Output time step to plot (index into the NetCDF file's `time` dimension)
- `center` Tuple `(<lon>, <lat>)`, map projection center
- `min_max` Tuple `(<min>, <max>)` fixed colorbar range; omit for an automatic range
- `save` Path to save the figure to (e.g. `"test.png"`); omit to display it interactively instead

## Development

Run the test suite with:
```bash
uv run pytest
```

Build the documentation with:
```bash
cd docs && uv run make html
```

## License

MIT - see [LICENSE.md](LICENSE.md).
