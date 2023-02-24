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
    'figure.subplot.wspace'  : 0.05,
    'figure.subplot.hspace'  : 0.25,
    'figure.dpi' : 200,
    'lines.markersize' : 6,
    'lines.linewidth' : 2.
}

matplotlib.rcParams.update(params)

arrowkwargs1 = {
        "head_width": 0.20,
        "head_length": 1.80,
        "linewidth": 1,
        "facecolor": 'k',
        }
arrowkwargs2 = {
        "head_width": 1.5,
        "head_length": 0.2,
        "linewidth": 1,
        "facecolor": 'k',
        }
arrowkwargs3 = {
        "head_width": 1.25,
        "head_length": 2.5,
        "linewidth": 1,
        "facecolor": 'k',
        }
arrowkwargs4 = {
        "head_width": 2.5,
        "head_length": 1.25,
        "linewidth": 1,
        "facecolor": 'k',
        }

fig = plt.figure(figsize=(9, 2.5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)



xmin = 1.
xL = 30
xR = 60
xmax = 100.
tmin = 0.
tmax = 100.
x = np.linspace(xmin, xmax, 1000)

uL = 2
uR = 12


shift = 1.5
ymin1 = 0.5 * uL

# x axis
ax1.arrow(0., 1.1*ymin1, xmax*1.1-xmin, 0., **arrowkwargs1)
# t axis
ax1.arrow(0., 1.1*ymin1, 0, 0.9 * uR, **arrowkwargs2)

ax1.text(xmax*1.2, 1.1*ymin1, r"$x$",
    verticalalignment="center",
    horizontalalignment='center',)

ax1.text(0., uR*1.1,  r"$u_0$",
    verticalalignment="bottom",
    horizontalalignment='center',)

ax1.plot([xL, xL], [0.8*ymin1, uL], lw=1, c="k", ls=":")
ax1.text(xL-shift, ymin1, r"$x_L$",
    verticalalignment="top",
    horizontalalignment='left',)

ax1.plot([xR, xR], [0.8*ymin1, uR], lw=1, c="k", ls=":")
ax1.text(xR-shift, ymin1, r"$x_R$",
    verticalalignment="top",
    horizontalalignment='left',)




ax1.text(0.5 * xL, 0.3 * uR,  r"$u_L$",
    verticalalignment="bottom",
    horizontalalignment='center',)

ax1.text(1.2 * xR, 0.6 * uR,  r"$u_R$",
    verticalalignment="bottom",
    horizontalalignment='center',)


ymin2 = -1

# x axis
ax2.arrow(0., ymin2, 1.01*xmax, 0., **arrowkwargs4)
# t axis
ax2.arrow(0., ymin2, 0, 0.99 * tmax, **arrowkwargs3)

ax2.text(xmax*1.07, ymin2, r"$x$",
    verticalalignment="center",
    horizontalalignment='center',)

ax2.text(0., tmax*1.1,  r"$t$",
    verticalalignment="bottom",
    horizontalalignment='center',)

ax2.text(xL-shift, ymin2, r"$x_L$",
    verticalalignment="top",
    horizontalalignment='left',)

ax2.text(xR-shift, ymin2, r"$x_R$",
    verticalalignment="top",
    horizontalalignment='left',)




def u(x):
    u = uL + (uR - uL)/(xR  - xL) * (x - xL)
    u[x < xL] = uL
    u[x > xR] = uR

    return u


ax1.plot(x, u(x), c="k")

x_characteristics = np.linspace(xmin+2, xmax, 30)
t_characteristics = np.linspace(tmin, tmax, 10000)
a = u(x_characteristics)

scale = 0.15

for i in range(x_characteristics.shape[0]):
    xc = x_characteristics[i] + a[i] * t_characteristics * scale
    mask = xc < xmax
    ax2.plot(xc[mask], t_characteristics[mask], c="k", lw=1)

xhead = xR + u(np.ones(1)*xR) * t_characteristics * scale
mask = xhead < xmax
ax2.plot(xhead[mask], t_characteristics[mask], c="b")

xtail = xL + u(np.ones(1)*xL) * t_characteristics * scale
mask = xtail < xmax
ax2.plot(xtail[mask], t_characteristics[mask], c="r")


ax1.set_xlim(-1., 1.5*xmax)
ax1.set_ylim(0.25*ymin1, 1.2*uR)


ax2.set_xlim(-1, 1.1*xmax)
ax2.set_ylim(4*ymin2, 1.2* tmax)


ax1.axis("off")
ax2.axis("off")


#  plt.show()
plt.savefig("rarefaction_characteristics.pdf")

