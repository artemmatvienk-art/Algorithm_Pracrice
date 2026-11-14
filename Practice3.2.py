import math

a = float(input("Перша сторона: "))
b = float(input("Друга сторона: "))
c = float(input("Третя сторона: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("Площа:", area)
else:
    print("Такого трикутника не існує")