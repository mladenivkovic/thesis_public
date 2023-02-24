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

fig = plt.figure(figsize=(6, 3))
ax = fig.add_subplot(111)
#  ax.plot([-10, 10], [0, 0], 'k')
#  ax.plot([0, 0], [0, 10], 'k', lw=1)
ax.arrow(-10, 0, 20, 0, **arrowkwargs)
ax.arrow(0, 0, 0, 10, **arrowkwargs)

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

plt.text(-5, 5, r"$\mathcal{U}_L$", 
    horizontalalignment='center',
    verticalalignment="center",)
plt.text(5, 5, r"$\mathcal{U}_R$", 
    horizontalalignment='center',
    verticalalignment="center", )


plt.savefig("riemann_problem.pdf")

