"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

res = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
prof = res - costs

if prof > 0:
    print(f"Финансовый результат - прибыль. Ее величина: {prof}")

    print("Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)")
    ren = prof / res
    print(f"Рентабельность выручки = {ren}")

    emp_num = int(input("Введите численность сотрудников фирмы: "))
    emp_pr = prof / emp_num
    print(f"Прибыль фирмы в расчете на одного сотрудника = {emp_pr}")

elif prof < 0:
    print(f"Финансовый результат - убыток. Ее величина: {prof}")

else:
    print("Выручка равна издержкам")