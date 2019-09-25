import numpy as np
import matplotlib.pyplot as plt

functionx = lambda x : np.cos(x) + x**3

def integral(a, b, tramos):
    h = (b - a) / tramos
    x = a
    suma = functionx(x)
    for i in range(0, tramos - 1, 1):
        x = x + h
        suma = suma + 2 * functionx(x)
    suma = suma + functionx(b)
    area = h * (suma / 2)
    return area

a = 1
b = 10
tramos = 10

print(integral(a, b, tramos))

for i in range(1, tramos):
    print("tramos ", i, "area ", integral(a, b, i))