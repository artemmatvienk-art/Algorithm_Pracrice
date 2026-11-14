text = input("Введіть текст: ")

letters = 0
digits = 0
other = 0

for char in text:
    code = ord(char)

    if 65 <= code <= 90 or 97 <= code <= 122:
        letters += 1
    elif 48 <= code <= 57:
        digits += 1
    else:
        other += 1

print("Літери:", letters)
print("Цифри:", digits)
print("Інші символи:", other)