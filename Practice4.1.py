permissions = int(input("Введіть маску прав: "))

print("Читання:", bool(permissions & 1))
print("Запис:", bool(permissions & 2))
print("Видалення:", bool(permissions & 4))
print("Адміністратор:", bool(permissions & 8))

permissions = permissions | 1
print("Додали читання:", permissions)

permissions = permissions & ~2
print("Забрали запис:", permissions)

permissions = permissions ^ 4
print("Змінили видалення:", permissions)