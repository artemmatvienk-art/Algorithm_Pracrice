numbers = [14, 27, 35, 42, 58, 63, 79]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)