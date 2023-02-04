'''
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
'''

my_file = open('text_2.txt', 'r')
content = my_file.read()
print(f'Text: \n {content}')
my_file = open('text_2.txt', 'r')
content = my_file.readlines()
print(f'Number of strings: - {len(content)}')
my_file = open('text_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Number of symbols in the {i + 1} - string {len(content[i])}')
my_file = open('text_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Number of words - {len(content)}')
my_file.close()