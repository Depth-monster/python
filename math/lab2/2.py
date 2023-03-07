#2
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

phi = np.linspace(0, 2*np.pi, 1000)
r = 4*np.cos(4*phi)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)
ax.plot(phi, r)
plt.show()

a, b = 0, np.pi/8
S = 0.5 * integrate.quad(lambda phi: (4*np.cos(4*phi))**2, a, b)[0]
print(f"The area of the figure is approximately {S:.3f} square units.")
