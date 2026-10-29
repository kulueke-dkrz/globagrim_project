from .constants import global_const
from . import driver


def run(**kwargs):
    """Integrate the model forward in time and write the result to NetCDF.

    All parameters are optional; any parameter you omit keeps whatever
    value it had on the previous call (the first call uses the built-in
    defaults from :mod:`globagrim.constants`).

    :param int NJ: Number of west-east circles of longitude.
    :param int NK: Number of north-south circles of latitude.
    :param int NL: Number of vertical levels.
    :param float TF: Total integration time, in hours.
    :param float DT: Integration time step, in seconds.
    :param int IEXP: Experiment number selecting the initial condition -
        ``1`` low pressure system over the Pacific, ``2`` flow over an
        isolated mountain in North America, ``3`` random wind field.
    :param float INT: Output interval in hours; ``0`` (the default) writes
        every time step.
    :param str OUT: Output NetCDF file path.
    """
    global_const.IEXP = kwargs.get("IEXP", global_const.IEXP)

    global_const.NJ = kwargs.get("NJ", global_const.NJ)
    global_const.NK = kwargs.get("NK", global_const.NK)
    global_const.NL = kwargs.get("NL", global_const.NL)

    global_const.DT = kwargs.get("DT", global_const.DT)
    global_const.TF = kwargs.get("TF", global_const.TF)

    global_const.output_int = kwargs.get("INT", 0) 

    global_const.output_path = kwargs.get("OUT", global_const.output_path)

    driver.globagrim()


def plot(**kwargs):
    """Plot one field from the NetCDF file written by the preceding run().

    :meth:`run` must have been called at least once before calling this,
    since it reads back the file that call wrote. All parameters are
    optional.

    :param str var_name: Field to plot - ``SE`` (surface elevation),
        ``PSG`` (sea level pressure), ``T`` (temperature), ``U`` (zonal
        wind), or ``V`` (meridional wind).
    :param int out_step: Output time step to plot (index into the NetCDF
        file's ``time`` dimension).
    :param tuple center: ``(lon, lat)`` map projection center.
    :param tuple min_max: ``(min, max)`` fixed colorbar range; omit for an
        automatic range.
    :param str save: Path to save the figure to; omit to display it
        interactively instead.
    """
    from . import visualization

    var_name = kwargs.get("var_name", "PSG")
    time_step = kwargs.get("out_step", 0)
    center = kwargs.get("center", (-180.0, 0.0))
    min_max = kwargs.get("min_max", None)
    save = kwargs.get("save", None)

    visualization.plot(var_name, time_step, center, min_max, save)
