#!/usr/bin/env python3


#-------------------------------------
# draws the new potentials plot.
# Usage:
#   ./draw_potentials.py
#-------------------------------------

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
params = {
    "font.size": 12,
    "font.family": "serif",
    "font.serif": "DejaVu Sans",
    "text.usetex": True,
    "figure.dpi": 200,
    "lines.markersize": 6,
    "lines.linewidth": 2.0,
}

matplotlib.rcParams.update(params)




xmin = -10.
xmax = 24.
xintersect = 5.6

xleft = np.linspace(xmin, xintersect*0.99, 1000)
xright = np.linspace(xintersect, xmax, 1000)

def phiA(x):
    return -14. * np.exp(-(x-12.)**2/40) - 0.75

def xofPhiA(phi, sign):
    """ 
    find x at which phiA(x) = phi
    just the inverse function of phiA(x)

    sign: +1 or -1, for whichever value of the 
    square root you want
    """

    return 12 + sign * np.sqrt( - 40. * np.log((phi + 0.75) / -14.))

def phiB(x):
    return -10. * np.exp(-(x-2)**2/20) - 0.5

def xofPhiB(phi, sign):
    """ 
    find x at which phiA(x) = phi
    just the inverse function of phiA(x)

    sign: +1 or -1, for whichever value of the 
    square root you want
    """

    return 2 + sign * np.sqrt( - 20. * np.log((phi + 0.5) / -10.))


fig = plt.figure(figsize = (8, 4), dpi=200)

ax = fig.add_subplot(111)#, aspect='equal')
#  ax = fig.add_subplot(111, aspect='equal')
ax.axis('off')
ax.set_xlim(xmin*1.6, xmax*1.2)

# potentials
ax.plot(xleft, phiB(xleft), 'b')
ax.plot(xright, phiA(xright), 'r')

# particles line
phiB_part = -8.6
ax.plot([xofPhiB(phiB_part, -1), xofPhiB(phiB_part, 1)], [phiB_part, phiB_part], 'b', lw=1)
phiA_part = -11.6
ax.plot([xofPhiA(phiA_part, -1), xofPhiA(phiA_part, 1)], [phiA_part, phiA_part], 'r', lw=1)
phiC_part = -2.8
ax.plot([xofPhiB(phiC_part, -1), xofPhiA(phiC_part, 1)], [phiC_part, phiC_part], 'forestgreen', lw=1)

# axis
plt.arrow(xmin*1.25, 0, xmax*1.05 - xmin*1.25, 0, color='k', linewidth=0.5, head_width=0.2)
plt.arrow(xmin*1.15, -15, 0, 16, color='k', linewidth=0.5, head_width=0.2)

# dotted lines for annotations
ax.plot([xmin*1.25, xintersect], [phiA(xintersect), phiA(xintersect)], 'k--', linewidth=0.5)

# points for particles
ax.scatter([10.3], [-11.6], color='r', s=8)
ax.scatter([2.64], [-8.6], color='b', s=8)
ax.scatter([15.3], [-2.8], color='forestgreen', s=8)

# annotations
ax.annotate(r"$0$", [xmin*1.35, 0], usetex=True, va='center')
ax.annotate(r"$x$", [xmax*1.1, 0], usetex=True, va='center')
ax.annotate(r"$\Phi_S$", [xmin*1.4, phiA(5.6)], usetex=True, va='center')
ax.annotate(r"$\Phi(x)$", [xmin*1.15, 1.9], usetex=True, ha='center')
dy = 0.2
ax.annotate(r"$P_A$", [10.3, -11.6+dy], color='r', va='bottom', ha='right')
ax.annotate(r"$P_B$", [2.64, -8.6+dy], color='b', va='bottom', ha='right')
ax.annotate(r"$P_C$", [15.3, -2.8+dy], color='forestgreen', va='bottom', ha='right')

ax.annotate(r"Clump $B$", [2., -15.5], color='b', va='top', ha='center')
ax.annotate(r"Clump $A$", [12., -15.5], color='r', va='top', ha='center')


plt.tight_layout()
plt.savefig("potentials_new.pdf")
