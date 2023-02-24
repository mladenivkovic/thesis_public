#!/usr/bin/env python3

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
    'figure.subplot.left'    : 0.06,
    'figure.subplot.right'   : 0.99,
    'figure.subplot.bottom'  : 0.15,
    'figure.subplot.top'     : 0.97,
    'figure.subplot.wspace'  : 0.15,
    'figure.subplot.hspace'  : 0.25,
    'figure.dpi' : 200,
    'lines.markersize' : 6,
    'lines.linewidth' : 2.
}

matplotlib.rcParams.update(params)



fig = plt.figure(figsize=(12, 3))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)


xmin = 1.
xmax = 100.
tmin = 0.
tmax = 100.
x = np.linspace(xmin, xmax, 1000)

def u(x):
    width = 5.
    amp = 0.5
    loc = 30
    amp2 = 5.e-8
    return amp * np.exp(-(x-loc)**2/(2*width)**2) - amp2 * (x-loc)**4 + x/xmax - 0.3



ax1.plot(x, u(x))

x_characteristics = np.linspace(xmin, xmax, 100)
t_characteristics = np.linspace(tmin, tmax, 10)

for xc in x_characteristics:
    a = u(xc)
    xc_all = xc + a * t_characteristics

    ax2.plot(xc_all, t_characteristics, c="k", lw=1)

ax1.set_xlim(xmin, xmax)
ax1.set_ylim(-0.55, 0.55)
ax2.set_xlim(xmin, xmax)
ax2.set_ylim(tmin, tmax)
ax1.set_xlabel(r"$x$")
ax2.set_xlabel(r"$x$")
ax1.set_ylabel(r"$u(x, t=0)$")
ax2.set_ylabel(r"$t$")



#  plt.show()
plt.savefig("burgers_characteristics.pdf")






