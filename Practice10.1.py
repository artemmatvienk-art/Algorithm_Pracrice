def power(a, n):
    if n == 0:
        return 1

    result = power(a, n // 2)

    if n % 2 == 0:
        return result * result
    else:
        return a * result * result


a = float(input("Основа: "))
n = int(input("Степінь: "))

if n >= 0:
    print("Результат:", power(a, n))
else:
    print("Результат:", 1 / power(a, -n))