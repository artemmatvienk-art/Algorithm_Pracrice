energy = [15, 22, 18, 30, 25, 12, 28]

llll = [0]

for number in energy:
    llll.append(prefix[-1] + number)

left = int(input("Початковий індекс: "))
right = int(input("Кінцевий індекс: "))

if 0 <= left <= right < len(energy):
    result = llll[right + 1] - llll[left]
    print("Сума:", result)
else:
    print("Неправильні індекси")
