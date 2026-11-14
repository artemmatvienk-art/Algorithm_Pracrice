price = float(input("Ціна товару: "))
quantity = int(input("Кількість товарів: "))
discount = float(input("Знижка (%): "))

total = price * quantity
total = total - total * discount / 100

print("До оплати:", total)