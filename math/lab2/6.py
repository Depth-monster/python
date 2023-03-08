#6
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функция, описывающая границы фигуры
def f1(x):
    return np.sin(np.pi*x/2)

def f2(x):
    return x**2

# Определяем границы интегрирования
a = 0
b = 1

# Вычисляем интеграл
def integrand(x):
    return (f1(x)**2 - f2(x)**2)*np.pi

V, _ = quad(integrand, a, b)

# Выводим результат
print(f"Объем тела: {V}")

# Рисуем график фигуры
x = np.linspace(a, b, 100)
plt.plot(x, f1(x), label='y=sin((pi*x)/2)')
plt.plot(x, f2(x), label='y=x^2')
plt.fill_between(x, f1(x), f2(x), alpha=0.2)
plt.legend()
plt.show()
