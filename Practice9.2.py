def convert(amount, rate):
    assert amount >= 0
    assert rate > 0

    return amount * rate


amount = float(input("Введіть суму: "))
rate = float(input("Введіть курс: "))

try:
    print("Результат:", round(convert(amount, rate), 2))
except AssertionError:
    print("Помилка введення")