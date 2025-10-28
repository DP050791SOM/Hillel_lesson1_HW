sec = int(input("Введите количество секунд (от 0 до 8640000): "))

dys, rem = divmod(sec, 24 * 60 * 60)
hur, rem = divmod(rem, 60 * 60)
mints, sec = divmod(rem, 60)

if dys % 10 == 1 and dys % 100 != 11:
    day = "день"
elif dys % 10 in (2, 3, 4) and not (12 <= dys % 100 <= 14):
    day = "дня"
else:
    day = "дней"

print(f"{dys} {day}, {hur:02d}:{mints:02d}:{sec:02d}")