# Индивидуальное задание 1, вариант 9
# Даны координаты трёх неколлинеарных точек.
# Вычислить периметр и площадь треугольника.

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

side_a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
side_b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
side_c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

perimeter = side_a + side_b + side_c

half_perimeter = perimeter / 2
area = math.sqrt(
    half_perimeter * (half_perimeter - side_a)
    * (half_perimeter - side_b) * (half_perimeter - side_c)
)

print(f"Периметр: {perimeter:.2f}")
print(f"Площадь: {area:.2f}")