list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [1, 2]

# list_1 = [1, 2]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


final_dict = {}

while True:
    try:
        key = list_1.pop(0)
    except IndexError:
        break

    try:
        value = list_2.pop(0)
    except IndexError:
        value = None

    final_dict[key] = value

print(final_dict)
