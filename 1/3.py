"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число
Считаем 3 + 33 + 333 = 369. """

n = int(input("Введите ваше число: "))

res = n + n * 11 + n * 111
print(f"n + nn + nnn = {res}")
