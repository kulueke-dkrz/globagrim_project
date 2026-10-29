from netCDF4 import Dataset

from globagrim import model


def test_run_recomputes_time_steps_each_call(tmp_path):
    # Regression test: a second model.run() call used to silently reuse the
    # first call's timestep count because it was cached at module import
    # time instead of recomputed from the current TF/DT.
    out1 = tmp_path / "run1.nc"
    out2 = tmp_path / "run2.nc"

    model.run(NJ=18, NK=9, TF=0.025, DT=15.0, OUT=str(out1))
    model.run(NJ=18, NK=9, TF=0.1, DT=15.0, OUT=str(out2))

    with Dataset(out1) as ds1, Dataset(out2) as ds2:
        n1 = ds1.dimensions["time"].size
        n2 = ds2.dimensions["time"].size

    assert n2 > n1


def test_run_handles_grid_size_change_across_runs(tmp_path):
    # Regression test: calling model.run() with a different grid size than
    # a previous call in the same session used to crash with a
    # "could not broadcast" ValueError, because state arrays were sized
    # once at first import rather than rebuilt per run.
    model.run(NJ=18, NK=9, TF=0.0, OUT=str(tmp_path / "small.nc"))
    model.run(NJ=36, NK=18, TF=0.0, OUT=str(tmp_path / "big.nc"))


def test_plot_does_not_raise(tmp_path):
    # Regression test: model.plot() used to raise NameError because the
    # `visualization` import in model.py was commented out.
    out = tmp_path / "plot_run.nc"
    png = tmp_path / "plot.png"

    model.run(NJ=18, NK=9, TF=0.0, OUT=str(out))
    model.plot(save=str(png))

    assert png.exists()
