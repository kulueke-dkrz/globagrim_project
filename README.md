
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcoKulueke/globagrim_project/HEAD)

# Global Atmospheric Grid Point Model

![logo](https://github.com/MarcoKulueke/globagrim_project/blob/main/png/logo.png?raw=true)

This model is inspired by GLOBAGIM of CLISAP (more information can be found via: https://www.clisap.de/research/b:-climate-manifestations-and-impacts/crg-dynamical-systems/models/globagim/)

## Installation
Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then from the repository root run:
```
uv sync
```
This creates a `.venv` with GLOBAGRIM and all dependencies installed, pinned exactly per `uv.lock`.
Then, run commands inside the environment with `uv run`, e.g.:
```
uv run python
```
or activate it directly with:
```
source .venv/bin/activate
```
To also install the development/docs extras (`jupyter`, `pytest`, `sphinx`), run `uv sync --extra dev` instead.

---
### Alternative
If you already have `numpy`, `xarray`, `netcdf4`, `matplotlib`, `cartopy`, `numba`, `pip` installed, you could add the GLOBAGRIM package to your current environment by executing:
```
pip install git+https://github.com/MarcoKulueke/globagrim_project.git#egg=globagrim
```
---

## Example Usage

Import the model from globagrim:

```
from globagrim import model
```

You can run the model with the following parameters:
- `NJ` Number of west-east circles of longitude
- `NK` Number of north-south circles of latitude
- `NL` Number of vertical levels 
- `TF` Total integration time in hours
- `DT` Integration time step in seconds
- `IEXP` Experiment number (`1` low pressure system over the pacific, `2`stream over montain in North America, `3`Random wind field)
- `INT` Output intervall in hours
- `OUT` Output path and file name

All parameters are optional. If you do not pass any parameters the default parameters will be used.

Below you can see an example call with default parameters:
```
model.run()
```

You can visualize the results with:
```
model.plot()
```
Again, all parameters are optional. You can specify the visualization with the following parameters:
- `var_name` String variable name (`SE`, `PSG`, `T`, `U`, `V`)
- `out_step` Integer output time step
- `center` Tuple `(<lon>,<lat>)` for center of visualization
- `min_max` Tuple `(<min>,<max>)` for a fixed colorbar
- `save` String (e.g. `test.png`)
