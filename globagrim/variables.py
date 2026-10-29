import numpy as np
from .constants import global_const

#
# string variables
#
class GLOBAL_STR:
    start_time = "18.09.2010 01:55:19"
    # cmon = "dec"  # month
    # cday = "30"  # day
    # chour = "00"  # hour
    # cmin = "00"  # minute

global_str = GLOBAL_STR()

#
# integer variables
#
class GLOBAL_INT:
    def __init__(self):
        self.nyear = 2014  # year
        self.nmonth = 12  # month
        self.nday = 30  # day
        self.nhour = 0  # hour
        self.nmin = 0  # minutes
        #
        # float variables
        #
        self.ti = 0.0  # model time in seconds
        #
        # scalars
        #
        self.dy = np.nan
        self.dsig = np.nan
        self.ntout = 0  # model output step

    def reset(self):
        # recompute every field from scratch so a new model.run() in the
        # same session doesn't inherit state left over from a previous run
        self.__init__()

global_int = GLOBAL_INT()
#
# arrays
#
class GLOBAL_ARRAY:
    def __init__(self):
        #
        # 1D arrays
        #
        self.flam_deg = np.full(global_const.NJ + 2, np.nan)  # longitude of grid points (deg)
        self.phi_deg = np.full(global_const.NK + 2, np.nan)  # latitude of grid points (deg)
        self.flam = np.full(global_const.NJ + 2, np.nan)  # longitude of grid points (rad)
        self.phi = np.full(global_const.NK + 2, np.nan)  # latitude of grid points (rad)
        self.dx = np.full(global_const.NK + 2, np.nan)  # zonal grid point distance (metric)
        self.cs = np.full(global_const.NK + 2, np.nan)  # cosinus latitude
        self.sn = np.full(global_const.NK + 2, np.nan)  # sinus latitude
        self.f = np.full(global_const.NK + 2, np.nan)  # coriolis parameter
        self.sigma = np.full(global_const.NL + 1, np.nan)  # SIGMA on full levels
        self.sigmah = np.full(global_const.NL, np.nan)  # SIGMA on half levels
        self.alp = np.full(global_const.NL, np.nan)  # height dependent coeffizient alpha
        self.gp0 = np.full(global_const.NL, np.nan)  # reference geopotential
        #
        # 2d arrays
        #
        self.ps = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2]
        )  # surfance pressure anomaly
        self.psn = np.zeros([global_const.NJ + 2, global_const.NK + 2])  # ps future
        self.pst = np.zeros([global_const.NJ + 2, global_const.NK + 2])  # Trend ps
        self.psg = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2]
        )  # absolute surface pressure
        self.phis = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2]
        )  # geopotential at surface (orography)
        #
        # 3d arrays with boundary conditions
        #
        self.u = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # mass-weighted zonal wind
        self.v = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # mass-weighted meridional wind
        self.t = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # mass-weighted temperature
        self.un = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # U future
        self.vn = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # V future
        self.tn = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # T future
        self.psa = np.zeros([global_const.NJ + 2, global_const.NK + 2])  # ps past
        self.ua = np.zeros([global_const.NJ + 2, global_const.NK + 2, global_const.NL])  # U past
        self.va = np.zeros([global_const.NJ + 2, global_const.NK + 2, global_const.NL])  # V past
        self.ta = np.zeros([global_const.NJ + 2, global_const.NK + 2, global_const.NL])  # T past
        self.ut = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # trend U
        self.vt = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # trend V
        self.tt = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # trend T
        self.uw = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # true zonal wind
        self.vw = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # true meridional wind
        self.tw = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # true temperature
        self.gp = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # geopotential
        ###########################
        # 3d arrays without boundary condiitons (index 0, NK +1 and NJ +1 are left empty)
        ###########################
        self.dsdt = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # SIGMA vertical velocity
        self.comp = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # adiabatic compression heat
        self.apx = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # zonal pressure gradient
        self.apy = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # meridional pressure gradient
        self.acx = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # zonal coriolis force
        self.acy = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # meridional coriolis force
        self.d = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # divergence of mass-weighted wind
        self.dm = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # divergence of mass flow
        self.du = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # zonal divergence of momentum
        self.dv = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # meridional divergence of momentum
        self.dvt = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # divergence of temperature flow
        self.vdivu = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # divergence of vertiacl U-flow
        self.vdivv = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # divergence of vertiacl V-flow
        self.vdivt = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # divergence of vertiacl T-flow
        self.diffu = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # diffusion of zonal momentum
        self.diffv = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # diffusion of meridional momentum
        self.difft = np.zeros(
            [global_const.NJ + 2, global_const.NK + 2, global_const.NL]
        )  # diffuson of temperature

    def reset(self):
        # recompute every array from scratch, matching the current
        # global_const.NJ/NK/NL, so a new model.run() in the same session
        # doesn't reuse (or overflow) arrays sized for a previous run
        self.__init__()

global_array = GLOBAL_ARRAY()
