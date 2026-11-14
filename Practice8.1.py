prices = [125, 140, 115, 160, 135, 180, 155, 170]

size = int(input("Розмір вікна: "))

if 0 < size <= len(prices):
    total = sum(prices[:size])
    max_sum = total
    min_sum = total

    for i in range(size, len(prices)):
        total = total - prices[i - size] + prices[i]

        if total > max_sum:
            max_sum = total

        if total < min_sum:
            min_sum = total

    print("Максимальна сума:", max_sum)
    print("Мінімальна сума:", min_sum)
else:
    print("Неправильний розмір")