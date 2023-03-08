#4
import numpy as np
import matplotlib.pyplot as plt

# Определяем функции x(t) и y(t)
def x(t):
    return (t**3)/3 - t

def y(t):
    return t**2 + 2

# Определяем производные dx/dt и dy/dt
def dx_dt(t):
    return t**2 - 1

def dy_dt(t):
    return 2*t

# Определяем функцию для вычисления длины дуги
def arc_length(t1, t2, n):
    t = np.linspace(t1, t2, n)
    dt = t[1] - t[0]
    integrand = np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)
    return np.sum(integrand)*dt

# Вычисляем длину дуги
L = arc_length(0, 3, 1000)
print("Длина дуги: {:.4f}".format(L))

# Строим график кривой
t = np.linspace(0, 3, 1000)
plt.plot(x(t), y(t))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кривая заданная параметрически')
plt.show()
