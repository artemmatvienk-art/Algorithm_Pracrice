text = input("Введіть текст: ")

new_text = ""

for char in text:
    code = ord(char)

    if 65 <= code <= 90:
        char = chr(code + 32)

    new_text += char

left = 0
right = len(new_text) - 1
result = True

while left < right:
    if new_text[left] != new_text[right]:
        result = False

    left += 1
    right -= 1

print("Паліндром:", result)