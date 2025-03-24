from math import *

# площадь круга
sircle = lambda r: pi * r ** 2
print('площадь окружности равна', (sircle(2)))

# площадь прямоугольника
s_rectangle = lambda a, b: a * b
print('площадь прямоугольника равна', s_rectangle(10, 13))

# площадь трапеции
trapecia = lambda a, b, h: 0.5 * (a + b) * h
print('площадь трапеции равна', trapecia(7, 5, 3))
