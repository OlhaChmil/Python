
"""2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

sec = int(input("Введите секунды : "))

hrs = sec / 3600
mints = sec / 60

print(f"Время в формате ч:м:с - {hrs} : {mints} : {sec}")
