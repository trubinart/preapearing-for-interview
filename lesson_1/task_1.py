get_string = lambda result: '\n'.join(['\t'.join(str(item) for item in itm) for itm in result])


def create_table(a, b, string_function):
    matrix = []
    line = []

    for x in range(1, b + 1):
        if len(line) < 4:
            line.append(a * x)
        else:
            matrix.append(line)
            line = []
            line.append(a * x)
    matrix.append(line)

    result = string_function(matrix)
    print(result)

if __name__ == "__main__":
    create_table(2, 40, get_string)
