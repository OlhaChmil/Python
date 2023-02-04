'''
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных будет свидетельствовать пустая строка.
'''

my_f = open('text_1.txt', 'w')
line = input('Write your text \n')
while line:
    my_f.writelines(line)
    line = input('rite your text \n')
    if not line:
        break


my_f.close()
my_f = open('text_1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()