numbers = [23, 56, 12, 78, 34, 91, 45]

minimum = numbers[0]
maximum = numbers[0]
total = 0
count = 0

for number in numbers:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

    total += number
    count += 1

print("Мінімум:", minimum)
print("Максимум:", maximum)
print("Сума:", total)
print("Кількість:", count)
print("Середнє:", total / count)
print("Різниця:", maximum - minimum)