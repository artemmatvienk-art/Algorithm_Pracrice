import time

array1 = [12, 25, 37, 48, 59, 63, 74, 86]
array2 = [37, 48, 59, 70, 81, 92, 25]

start = time.time()

result1 = []

for number in array1:
    if number in array2 and number not in result1:
        result1.append(number)

time1 = time.time() - start

start = time.time()

result2 = list(set(array1) & set(array2))

time2 = time.time() - start

print("Перший результат:", result1)
print("Час першого способу:", time1)

print("Другий результат:", result2)
print("Час другого способу:", time2)