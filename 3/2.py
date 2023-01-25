
'''Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить 
вывод данных о пользователе одной строкой.
'''

def user_info(firstname, lastname, birthyear, city, email, phone):
    print(firstname, lastname, birthyear, city, email, phone)

user_info(
    firstname = input('Введите ваше имя: '),
    birthyear = input('Введите год вашего рождения: '),
    city = input('Введите ваш город: '),
    lastname = input('Введите вашу фамилию: '),
    email = input('Введите адрес вашей эл.почты: '),
    phone = input('Введите ваш телефон: '))

