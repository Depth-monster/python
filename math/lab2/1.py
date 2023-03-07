# задание 1

# Вычислить площадь фигуры, ограниченной кривыми, 
# заданными в декартовой системе координат на python: y=arcsin(x), y=arccos(x), y=0
import math
import scipy.integrate as spi

def f1(x):
    return math.asin(x)

def f2(x):
    return math.acos(x)

def f3(x):
    return 0

a = -1
b = 1

area1, _ = spi.quad(f1, a, b)
area2, _ = spi.quad(f2, a, b)
area3, _ = spi.quad(f3, a, b)

area = abs(area1 - area2) + area3

print("Площадь фигуры равна:", area)


