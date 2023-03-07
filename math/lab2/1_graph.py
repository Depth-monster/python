import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1000)

y1 = np.arcsin(x)
y2 = np.arccos(x)
y3 = np.zeros_like(x)

plt.plot(x, y1, label="y = arcsin(x)")
plt.plot(x, y2, label="y = arccos(x)")
plt.plot(x, y3, label="y = 0")
plt.fill_between(x, y1, y2, where=y1>y2, color="gray", alpha=0.5)
plt.legend()
plt.show()
