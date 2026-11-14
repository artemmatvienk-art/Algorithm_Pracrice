import time

numbers = list(range(500000))
numbers_set = set(numbers)

target = 345678

start = time.time()
result1 = target in numbers
time1 = time.time() - start

start = time.time()
result2 = target in numbers_set
time2 = time.time() - start

print("Пошук у списку:", time1)
print("Пошук у множині:", time2)

print("Результат списку:", result1)
print("Результат множини:", result2)