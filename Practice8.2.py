energy = [15, 22, 18, 30, 25, 12, 28]

prefix = [0]

for number in energy:
    prefix.append(prefix[-1] + number)

left = int(input("Початковий індекс: "))
right = int(input("Кінцевий індекс: "))

if 0 <= left <= right < len(energy):
    result = prefix[right + 1] - prefix[left]
    print("Сума:", result)
else:
    print("Неправильні індекси")