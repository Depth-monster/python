from scipy import integrate

def dydx(x):
    return -x / np.sqrt(1 - x**2) + 1 / np.sqrt(1 - x**2)

a, b = 0, 7/9
L = integrate.quad(lambda x: np.sqrt(1 + dydx(x)**2), a, b)[0]
print(f"The length of the curve is approximately {L:.3f} units.")
