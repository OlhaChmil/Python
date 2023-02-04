'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить её на экран.
'''

def nmb_sum():
    try:
        with open('text_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error')
    except ValueError:
        print('Not a number')
nmb_sum()
