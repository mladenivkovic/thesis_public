#!/usr/bin/env python3

#-----------------------------------------------------------------
# Draw a plot representing the piecewise linear discretization
#-----------------------------------------------------------------



# First determine piecewise constant value in each cell
# then get gradient based on the neighbour's values


import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches


xmin = 0
xmax = 10
ymin = 0
ymax = 4
dx = 1.5
#  dx = 0.5


# some continuous nice looking function to draw
def f(x):
    return 2. + 1.3 * np.sin(x) * np.exp(-x/10)

def integral_f(x):
    return 2. * x - 1.28713 * np.exp(-0.1 * x) * np.cos(x) - 0.128713 * np.exp(-0.1 * x) * np.sin(x)



fig = plt.figure(figsize=(9,4.5))
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xticks([])
ax.set_yticks([])

# draw function
x = np.linspace(xmin, xmax, 500)
ax.plot(x, f(x), lw=3, color='k', ls="--", zorder=10, alpha=0.75)

# Shade background according to slope
#  x = xmin
#  while x < xmax:
#
#      Uprev = (integral_f(x) - integral_f(x-dx))/dx
#      Uthis = (integral_f(x+dx) - integral_f(x))/dx
#      Unext = (integral_f(x + 2*dx) - integral_f(x+dx))/dx
#
#      h_triangle = abs(Uprev - Unext)
#      A_triangle = dx * h_triangle / 2
#
#      h0 = (Uthis * dx - A_triangle) / dx
#
#      if Uprev > Unext:
#          yleft = h0 + h_triangle
#          yright = h0
#      else:
#          yleft = h0
#          yright = h0 + h_triangle
#
#      # draw shade
#      height = (integral_f(x+dx) - integral_f(x) ) / dx
#      ax.add_patch(patches.Polygon([(x, ymin), (x+dx, ymin), (x+dx, yright), (x, yleft)], fill=True, facecolor='darkgrey'))
#
#      # draw red line
#      ax.plot([x, x+dx], [yleft, yright], color='r')
#
#      # draw green line (equivalent to piecewise constant)
#      #  ax.plot([x, x+dx], [height, height], color='g')
#
#      x += dx
#      # draw grid
#      ax.plot([x, x], [ymin, ymax], ':', color='grey')

def state(U, slope, delta_x):
    return U + slope * delta_x 

# Shade constant 
x = xmin
while x < xmax:

    Uprev = (integral_f(x) - integral_f(x-dx))/dx
    Uthis = (integral_f(x+dx) - integral_f(x))/dx
    Unext = (integral_f(x + 2*dx) - integral_f(x+dx))/dx

    h_triangle = abs(Uprev - Unext)
    A_triangle = dx * h_triangle / 2

    h0 = (Uthis * dx - A_triangle) / dx

    # centered slope
    sc = 0.5 * (Unext - Uprev) / dx
    # upwind slope
    su = (Uthis - Uprev) / dx
    # downwind slope
    sd = (Unext - Uthis) / dx
        
    ax.plot([x, x+dx], [state(Uthis, sc, -0.5 * dx), state(Uthis, sc, 0.5*dx)], color='C0', lw=2)
    ax.plot([x, x+dx], [state(Uthis, su, -0.5 * dx), state(Uthis, su, 0.5*dx)], color='C1', lw=2)
    ax.plot([x, x+dx], [state(Uthis, sd, -0.5 * dx), state(Uthis, sd, 0.5*dx)], color='C2', lw=2)

    #
    #  if Uprev > Unext:
    #      yleft = h0 + h_triangle
    #      yright = h0
    #  else:
    #      yleft = h0
    #      yright = h0 + h_triangle

    # draw shade
    height = (integral_f(x+dx) - integral_f(x) ) / dx
    ax.add_patch(patches.Polygon([(x, ymin), (x+dx,ymin), (x+dx, Uthis), (x, Uthis)], fill=True, facecolor='darkgrey'))

    # draw red line
    #  ax.plot([x, x+dx], [yleft, yright], color='r')

    # draw green line (equivalent to piecewise constant)
    #  ax.plot([x, x+dx], [height, height], color='g')

    x += dx
    # draw grid
    ax.plot([x, x], [ymin, ymax], ':', color='grey')



# annotate
plt.figtext(0.175, 0.1, r"$\mathcal{U}_{i-3}$", usetex=True, fontsize=14)
plt.figtext(0.290, 0.1, r"$\mathcal{U}_{i-2}$", usetex=True, fontsize=14)
plt.figtext(0.405, 0.1, r"$\mathcal{U}_{i-1}$", usetex=True, fontsize=14)
plt.figtext(0.520, 0.1, r"$\mathcal{U}_{i}$", usetex=True, fontsize=14)
plt.figtext(0.625, 0.1, r"$\mathcal{U}_{i+1}$", usetex=True, fontsize=14)
plt.figtext(0.740, 0.1, r"$\mathcal{U}_{i+2}$", usetex=True, fontsize=14)
plt.figtext(0.07, 0.5, r"$\mathcal{U}(\mathbf{x})$", usetex=True, fontsize=14)

#  plt.show()
plt.savefig("piecewise_linear.pdf", form='pdf')
