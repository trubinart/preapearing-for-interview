import os


def read_file(file, check='', type_include=0, replace=0, replace_text=''):
    if replace == 1 and replace_text != '':
        with open(file, 'r') as f:
            old_data = f.read()

        new_data = old_data.replace(check, replace_text)

        with open(file, 'w') as f:
            f.write(new_data)

        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())

    if check is not False and type_include != 0:
        if type_include == 1:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().find(check) != -1:
                        print(line.strip())
                        break
        if type_include == 2:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().find(check) != -1:
                        print(line.strip())
    else:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())


def my_function(file, check='', type_include=0, replace=0, replace_text=''):
    if os.path.exists(file):
        print('Файл уже есть')

    list_1 = [i for i in range(0, 10)]
    list_2 = [i + k if i == 'a' else i for i in 'asdlaskjdkasjdlkajsdkl' for k in '12321345']

    data = zip(list_1, list_2)

    with open(file, 'w', encoding='utf-8') as f:
        for i in data:
            f.write(f'{i[0]} {i[1]} \n')

    read_file(file, check, type_include, replace, replace_text)


if __name__ == '__main__':
    my_function('file.txt', 'a', 2)
    my_function('file.txt', 'a', 2, 1, 'less')
