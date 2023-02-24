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



x0 = 3
x1 = 8
t0 = 3
t1 = 8
dx = 0.1

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)

# x axis
ax.arrow(0, 0, 10, 0, **arrowkwargs)
# t axis
ax.arrow(0, 0, 0, 10, **arrowkwargs)

# characteristic
ax.plot([0, 10], [0, 10], lw=2, c="r", zorder=5)

ax.plot([x0, x0], [-dx, t0], ls=":", lw=1, c='k', zorder=-1)
ax.plot([x1, x1], [-dx, t1], ls=":", lw=1, c='k', zorder=-1)

ax.plot([-dx, x0], [t0, t0], ls=":", lw=1, c='k', zorder=-1)
ax.plot([-dx, x1], [t1, t1], ls=":", lw=1, c='k', zorder=-1)

ax.axis("off")
# x label
plt.text(10.7, 0.0, r"$x$", 
    verticalalignment="center",
    horizontalalignment='center',)
# t label
plt.text(0, 11, r"$t$",
    verticalalignment="center",
    horizontalalignment='center',)

plt.text(2.5, 6, r"$\mathcal{U}_L$,\\$\mathcal{F}_L = \mathcal{F}(\mathcal{U}_L)$", 
    multialignment="left",
    horizontalalignment='center',
    verticalalignment="center")
plt.text(5.5, 2.5, r"$\mathcal{U}_R$,\\$\mathcal{F}_R = \mathcal{F}(\mathcal{U}_R)$", 
    multialignment="left",
    horizontalalignment='center',
    verticalalignment="center", )
plt.text(8.5, 9.5, r"$S$",
    horizontalalignment='center',
    verticalalignment="center", color="r")

plt.text(x0, -dx, r"$x_0$",
    horizontalalignment='center',
    verticalalignment="top")
plt.text(x1, -dx, r"$x_1$",
    horizontalalignment='center',
    verticalalignment="top")
plt.text(-dx, t0, r"$t_0$",
    horizontalalignment='right',
    verticalalignment="center")
plt.text(-dx, t1, r"$t_1$",
    horizontalalignment='right',
    verticalalignment="center")

#  plt.show()
plt.savefig("rankine_hugeniot.pdf")

