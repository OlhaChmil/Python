'''Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших
двух аргументов.'''

def my_func(*args):
    args1 = int(input("args1: "))
    args2 = int(input("args2: "))
    args3 = int(input("args3: "))

    if args1 >= args2 > args3:
        return args1 + args2
    elif args3 >= args2 > args1:
        return args3 + args2
    elif args1 >= args3 > args1:
        return args1 + args3


print(my_func())

'''def my_func(var_1, var_2, var_3):

    var_1 = int(input('Введите первое число: '))
    var_2 = int(input('Введите второе число: '))
    var_3 = int(input('Введите третье число: '))

    if var_1 >= var_3 and var_2 >= var_3:
        result = var_1 + var_2
        return result
    elif var_1 >= var_2 and var_3 >= var_2:
        result = var_1 + var_3
        return result
    else:
        result = var_2 + var_3
        return result

    my_func()'''