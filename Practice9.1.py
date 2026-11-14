def average(grades):
    return sum(grades) / len(grades)


def minimum(grades):
    return min(grades)


def maximum(grades):
    return max(grades)


def analyze(grades):
    if len(grades) == 0:
        return None

    return average(grades), minimum(grades), maximum(grades)


grades = [78, 92, 85, 67, 96]

result = analyze(grades)

if result:
    print("Середній бал:", result[0])
    print("Мінімальний бал:", result[1])
    print("Максимальний бал:", result[2])
else:
    print("Список порожній")