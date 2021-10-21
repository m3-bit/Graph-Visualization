import numpy as np
import matplotlib.pyplot as plt

# middle line
x1 = np.linspace(-2, 2, 100)
gx = 1/2 * np.cos(2 * np.pi * x1) + 7/2
plt.plot(x1, gx)

# top line
x2 = np.linspace(-1, 1, 100)
fx = x2 ** 4 -x2 **2 + 6
plt.plot(x2, fx, lw='3')

# left line
x3 = np.linspace(-7, -1, 100)
fx_left = 12 / (np.abs(x3) + 1)
plt.plot(x3, fx_left, lw='3')

# right line
x4 = np.linspace(1, 7, 100)
fx_right = 12 / (np.abs(x4) + 1)
plt.plot(x4, fx_right, lw='3')

plt.axis([-7, 7, 0, 7])
plt.title('Mt.Fuji')
plt.show()