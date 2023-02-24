#!/usr/bin/env python3

#---------------------------------------
# A simple plot to demonstrate how
# the flux correction method works
#---------------------------------------

from matplotlib import pyplot as plt
import numpy as np

rng = np.random.default_rng(2)
xp = rng.uniform(size=10, low=-1, high=1)
yp = rng.uniform(size=10, low=-1, high=1)


fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, aspect="equal")

ax.plot([0, 0], [-1, 1], c="k", lw=1)
ax.plot([-1, 1], [0, 0], c="k", lw=1)
ax.scatter([0], [0], c="k", marker="*", s=300, zorder=98)
ax.scatter([0], [0], c="orange", marker="*", s=200, zorder=99)
ax.scatter(xp, yp, c="C0", alpha=0.7, marker="o", s=100, zorder=99)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

ax.annotate("$w_1$", (0.5, 0.5), usetex=True)
ax.annotate("$w_2$", (-0.5, 0.5), usetex=True)
ax.annotate("$w_3$", (-0.5, -0.5), usetex=True)
ax.annotate("$w_4$", (0.5, -0.5), usetex=True)

plt.axis("off")
plt.tight_layout()
plt.savefig("flux_correction_method_plot.pdf")
