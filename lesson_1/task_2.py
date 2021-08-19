import os


def print_directory_contents(sPath):
    list_1 = os.listdir(sPath)

    for item in list_1:
        check_dir = os.path.isfile(f'{sPath}/{item}')
        if check_dir is False:
            print_directory_contents(f'{sPath}/{item}')
        else:
            print(f'Путь {sPath} | файл {item}')


if __name__ == "__main__":
    directory = '/Users/macbookair/Documents/1 - GeekBrains/preapearing-for-interview/preapearing-for-interview'
    print_directory_contents(directory)
