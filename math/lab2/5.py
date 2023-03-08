#5
import numpy as np
import matplotlib.pyplot as plt

# Задаем функцию r(phi)
def r(phi):
    return 8*np.sin(phi)

# Определяем начальный и конечный углы дуги
a = 0
b = np.pi/4

# Определяем шаг для построения графика
step = 0.01

# Создаем массив углов для построения графика
phi_vals = np.arange(a, b+step, step)

# Создаем массив радиусов для построения графика
r_vals = r(phi_vals)

# Строим график
plt.polar(phi_vals, r_vals)

# Вычисляем длину дуги
L = 2*np.pi

# Выводим результат
print("Длина дуги равна", L)

# Отображаем график
plt.show()
