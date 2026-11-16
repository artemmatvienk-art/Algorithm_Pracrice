binary = input("Введіть двійкове число: ")

number = 13

for digit in binary:
    number = number * 2 + int(digit)

print("Десяткове число:", number)
