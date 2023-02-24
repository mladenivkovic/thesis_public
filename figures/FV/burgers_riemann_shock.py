#!/usr/bin/env python3

#-----------------------------------------------------------------
# Create a plot for the Riemann IVP
#-----------------------------------------------------------------


import numpy as np
from matplotlib import pyplot as plt
import matplotlib

params = {
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'font.size': 16,
    'font.family': 'serif',
    'font.serif': 'DejaVu Sans',
    'legend.fontsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': True,
    'figure.subplot.left'    : 0.05,
    'figure.subplot.right'   : 0.97,
    'figure.subplot.bottom'  : 0.12,
    'figure.subplot.top'     : 0.92,
    'figure.subplot.wspace'  : 0.25,
    'figure.subplot.hspace'  : 0.25,
    'figure.dpi' : 200,
    'lines.markersize' : 6,
    'lines.linewidth' : 2.
}

matplotlib.rcParams.update(params)

arrowkwargs = {
        "head_width": 0.10,
        "linewidth": 1,
        "facecolor": 'k',
        }

fig = plt.figure(figsize=(12, 3))


UL = 6
UR = 3

xmin = 0
xmax = 10
xmid = 0.5 * (xmax + xmin)
ymin = 0
ymax = 10

def plot_riemann_problem(ax):
    ax.plot([xmid, xmid], [ymin, ymax], 'k', ls=":", lw=1)
    # x axis
    ax.arrow(xmin, ymin, xmax-xmin, 0, **arrowkwargs)
    # t axis
    ax.arrow(xmin, ymin, 0, ymax, **arrowkwargs)

    # U_L
    ax.plot([xmin, xmid], [UL, UL], "k")

    # U_R
    ax.plot([xmid, xmax], [UR, UR], "k")

    ax.axis("off")
    # origin
    ax.text(5, -1, r"0", 
        verticalalignment="center",
        horizontalalignment='center',)
    # x label
    ax.text(10.7, 0.0, r"$x$", 
        verticalalignment="center",
        horizontalalignment='center',)
    # t label
    ax.text(0, 11, r"$u_0(x)$",
        verticalalignment="center",
        horizontalalignment='center',)

    ax.text(2.5, 5, r"$u_L$", 
        horizontalalignment='center',
        verticalalignment="center",)
    ax.text(7.5, 2.5, r"$u_R$", 
        horizontalalignment='center',
        verticalalignment="center", )


def plot_characteristics(ax):
    # x axis
    ax.arrow(0, 0, 10, 0, **arrowkwargs)
    # t axis
    ax.arrow(xmid, ymin, 0, ymax-ymin, **arrowkwargs)

    # factor 1.5: for aesthetic reasons only.
    scale = 0.1
    UL_use = UL * 1.5 * scale
    UR_use = UR * scale

    def characteristic(x, a, t):
        return x + a*t

    x = np.linspace(0, 10, 20)
    a = np.ones(x.shape) * UL_use
    a[x > xmid] = UR_use

    for i in range(x.shape[0]):
        ax.plot([x[i], characteristic(x[i], a[i], ymax)], [ymin, ymax], c="k", lw=1)

    ax.set_xlim(xmin, xmax*1.02)
    ax.set_ylim(ymin, ymax*1.04)

    ax.axis("off")
    # origin
    ax.text(5, -1, r"0", 
        verticalalignment="center",
        horizontalalignment='center',)
    # x label
    ax.text(10.7, 0.0, r"$x$", 
        verticalalignment="center",
        horizontalalignment='center',)
    # t label
    ax.text(xmid, 11, r"$t$",
        verticalalignment="center",
        horizontalalignment='center',)




def plot_shock(ax):
    # x axis
    ax.arrow(0, 0, 10, 0, **arrowkwargs)
    # t axis
    ax.arrow(xmid, ymin, 0, ymax-ymin, **arrowkwargs)

    # factor 1.5: for aesthetic reasons only.
    scale = 0.1
    UL_use = UL * 1.5 * scale
    UR_use = UR * scale

    # shock speed
    S = 0.5 * (UL_use**2 - UR_use**2) / (UL_use - UR_use)

    def shock(x0, t):
        return x0 + S * t

    def characteristic(x, a, t):
        return x + a*t
    
    def characteristic_intersection_time(x0, xS, a, S, tmax):
        #  if x0 < xS:
        t_intersect = (xS - x0) / (a - S)
        if t_intersect > tmax:
            return tmax
        else:
            return t_intersect

        #  else:


    x = np.linspace(0, 10, 20)
    a = np.ones(x.shape) * UL_use
    a[x > xmid] = UR_use

    for i in range(x.shape[0]):
        t = characteristic_intersection_time(x[i], xmid, a[i], S, ymax)
        ax.plot([x[i], characteristic(x[i], a[i], t)], [ymin, t], c="k", lw=1)

    ax.plot([xmid, shock(xmid, ymax)], [ymin, ymax], c='r', lw=2, zorder=50)

    ax.set_xlim(xmin, xmax*1.02)
    ax.set_ylim(ymin, ymax*1.04)

    ax.axis("off")
    # origin
    ax.text(5, -1, r"0", 
        verticalalignment="center",
        horizontalalignment='center',)
    # x label
    ax.text(10.7, 0.0, r"$x$", 
        verticalalignment="center",
        horizontalalignment='center',)
    # t label
    ax.text(xmid, 11, r"$t$",
        verticalalignment="center",
        horizontalalignment='center',)




ax1 = fig.add_subplot(131)
plot_riemann_problem(ax1)

ax2 = fig.add_subplot(132)
plot_characteristics(ax2)

ax3 = fig.add_subplot(133)
plot_shock(ax3)

#  plt.show()
plt.savefig("burgers_riemann_shock.pdf")

