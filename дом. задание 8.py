from math import *  # импортируем математические функции


#  пишем функции вычисления площади фигур
def rectangle_area(length, width):
    return length * width


def treangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return pi * radius ** 2

    # вводим данные по выбору фигуры


figure = int(
    input('выберите фигуру для вычисления площади:\n 1 - прямоугольник,\n 2 - треугольник,\n 3 - круг\n ---> '))

# вычисляем площадь первой фигуры
if figure == 1:
    length = float(input('введите длину прямоугольника: '))  # на всякий случай, если число дробное
    width = float(input('введите ширину прямоугольника: '))
    s = rectangle_area(length, width)  # функция вычисления площади прямоугольника

    print(f'площадь прямоугольника составляет - {s}')  # выводим площадь прямоугольника
elif figure == 2:
    base = float(input('введите длину основания треугольника: '))  # на всякий случай, если число дробное
    height = float(input('введите высоту треугольника: '))
    s = treangle_area(base, height)  # функция вычисления площади треугольника
    print(f'площадь треугольника равна {s}')
elif figure == 3:
    radius = float(input('введите радиус для вычисления площади круга: '))  # на всякий случай, если число дробное
    s = circle_area(radius)  # функция вычисления площади круга
    print(f'площадь круга равна {s}')  # выводим площадь круга
