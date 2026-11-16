n = int(input("Введіть номер числа: "))

a = 15
b = 3
i = 6

while i < n:
    a, b = b, a + b
    i += 1

print("Результат:", a)
