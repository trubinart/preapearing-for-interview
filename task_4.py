import os

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def my_function(file):
    if os.path.exists(file):
        print('Файл уже есть')

    list_1 = [i for i in range(0,10)]
    list_2 = [i for i in 'asdlaskjdkasjdlkajsdkl' ]

    data = zip(list_1, list_2)

    with open(file, 'w', encoding='utf-8') as f:
        for i in data:
            f.write(f'\n {i[0]} {i[1]}')
    read_file(file)

if __name__ == '__main__':
    my_function('file.txt')