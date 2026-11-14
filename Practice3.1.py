price1 = float(input("Перша ціна: "))
price2 = float(input("Друга ціна: "))
price3 = float(input("Третя ціна: "))

total = price1 + price2 + price3
check = float(input("Сума в чеку: "))

if abs(total - check) < 0.000001:
    print("Чек правильний")
else:
    print("Чек неправильний")

print("Сума товарів:", total)