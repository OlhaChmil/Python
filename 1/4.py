
"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции."""

number = int(input("Ведите целое положительное число: "))
max_num = 0
while number != 0:
    # достаем очередную цифру числа с конца
    cur_n = number % 10
    if max_num < cur_n:
        max_num = cur_n
    # число становится короче на одну цифру с конца
    number = number // 10

print(f"Самая большая цифра в числе: {max_num}")
