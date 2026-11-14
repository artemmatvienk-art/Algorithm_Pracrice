def brackets(n, opened=0, closed=0, text=""):
    if len(text) == n * 2:
        print(text)
        return

    if opened < n:
        brackets(n, opened + 1, closed, text + "(")

    if closed < opened:
        brackets(n, opened, closed + 1, text + ")")


n = int(input("Кількість пар дужок: "))

if n > 0:
    brackets(n)
else:
    print("Введіть додатне число")