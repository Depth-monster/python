import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 7/9, 1000)
y = np.sqrt(1 - x**2) + np.arcsin(x)

fig = plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
