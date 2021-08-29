
def ask_number():
    ask = input('Введите число: ')
    if ask.find('.') == -1:
        print('Число целое')
    else:
        print('Число дробное')
        number_list = ask.split('.')
        if int(number_list[0]) == int(number_list[1]):
            print('Числа до и после точки совпадают')
        else:
            print('Числа до и после точки НЕ совпадают')

if __name__ == '__main__':
    ask_number()
