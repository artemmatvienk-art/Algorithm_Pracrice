number = int(input("Введіть тризначне число: "))

a = number // 100
b = number // 10 % 10
c = number % 10

result = c * 100 + b * 10 + a

print("Результат:", result)