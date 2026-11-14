n = int(input("Введіть номер числа: "))

a = 0
b = 1
i = 0

while i < n:
    a, b = b, a + b
    i += 1

print("Результат:", a)