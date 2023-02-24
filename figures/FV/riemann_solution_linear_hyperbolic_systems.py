#!/usr/bin/env python3

#-----------------------------------------------------------------
# Create a plot for the solution structure of the Riemann IVP
#-----------------------------------------------------------------


import numpy as np
from matplotlib import pyplot as plt
import matplotlib

params = {
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'font.size': 14,
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
    'lines.linewidth' : 1.
}

matplotlib.rcParams.update(params)

arrowkwargs = {
        "head_width": 0.10,
        "linewidth": 2,
        "facecolor": 'k',
        "zorder": 20
        }

xmin = -10
xmax = -xmin
ymin = 0
ymax = 10

fig = plt.figure(figsize=(6, 3))
ax = fig.add_subplot(111)
#  ax.plot([xmin, xmax], [0, 0], 'k', zorder=10)
#  ax.plot([0, 0], [ymin, ymax], 'k', zorder=10)
ax.arrow(xmin, ymin, (xmax - xmin), 0, **arrowkwargs)
ax.arrow(0, 0, 0, (ymax - ymin), **arrowkwargs)

def x_for_ymax(a):
    res = ymax/a
    if res > xmax:
        return xmax
    elif res < xmin:
        return xmin
    else:
        return res

def get_outer_point(a):
    """
    get the outer point for a line with slope a starting at (0, 0)
    the outer point is on the edge of the plot:
    either x = xmin or x = xmax and y < ymax, or y = ymax with xmin < x < xmax

    returns tuple [0, x_outer], [0, y_outer] so you can
    plug it directly into plots.
    """
    
    x = None
    y = None

    if a <= 0.:

        if a <= -1.: 
            # we touch the x=xmin edge
            x = xmin
            y = xmin / a

        elif a < 0.:
            # we're at the top of the plot
            y = ymax
            x = a*y

    else:

        if a <= 1.:
            # we're at the top of the plot
            y = ymax
            x = a*y

        else:
            x = xmax
            y = xmax / a



    return [0., x], [0., y]





for a in [-1., -0.6, -0.3, 0.5, 0.7, 1.2]:
    x, y = get_outer_point(a)
    ax.plot(x, y, "k--")


plt.text(xmin+0.5, ymax-2, r"$\lambda_1$",
    verticalalignment="center",
    horizontalalignment='center',)

plt.text(xmin+3.5, ymax, r"$\lambda_2$",
    verticalalignment="center",
    horizontalalignment='center',)

plt.text(xmax - 0.5, ymax - 3, r"$\lambda_m$",
    verticalalignment="center",
    horizontalalignment='center',)

ax.axis("off")
# axis
# origin
plt.text(0, -1, r"0",
    verticalalignment="center",
    horizontalalignment='center',)
# x label
plt.text(11., 0.0, r"$x$",
    verticalalignment="center",
    horizontalalignment='center',)
# t label
plt.text(0, 11, r"$t$",
    verticalalignment="center",
    horizontalalignment='center',)

# U_L
plt.text(-6, 2, r"$\mathcal{U}_L$",
    horizontalalignment='center',
    verticalalignment="center",)
# U_R
plt.text(6, 2, r"$\mathcal{U}_R$",
    horizontalalignment='center',
    verticalalignment="center", )


plt.savefig("riemann_solution_linear_hyperbolic_systems.pdf")

