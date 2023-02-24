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

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)

# x axis
ax.arrow(0, 0, 10, 0, **arrowkwargs)
# t axis
ax.arrow(0, 0, 0, 10, **arrowkwargs)

# characteristic
ax.plot([0, 10], [0, 8], lw=1, c="r", zorder=-1)

ax.axis("off")
# origin
plt.text(0, -1, r"0", 
    verticalalignment="center",
    horizontalalignment='center',)
# x label
plt.text(10.7, 0.0, r"$x$", 
    verticalalignment="center",
    horizontalalignment='center',)
# t label
plt.text(0, 11, r"$t$",
    verticalalignment="center",
    horizontalalignment='center',)

plt.text(2.5, 5, r"$u_L$", 
    horizontalalignment='center',
    verticalalignment="center",)
plt.text(7.5, 4., r"$u_R$", 
    horizontalalignment='center',
    verticalalignment="center", )
plt.text(8.5, 9, r"$x - at = 0$\\ characteristic", 
    horizontalalignment='center',
    verticalalignment="center", fontsize=12)

plt.savefig("riemann_solution_linear_advection.pdf")

