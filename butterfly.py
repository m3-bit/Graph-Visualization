import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 12 * np.pi, 0.01)
x = np.sin(t) * (np.e ** np.cos(t) -2 * np.cos (4 * t) - np.sin(t / 12) ** 5)
y = np.cos(t) * (np.e ** np.cos(t) -2 * np.cos (4 * t) - np.sin(t / 12) ** 5)

plt.plot (x, y)
plt.title('Butterfly')
plt.show ()