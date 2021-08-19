import random


def generate(a, b):
    final_list = []
    final_dict = {}
    num = 0

    for i in range(1, 10):
        num += 1
        x = random.randint(a, b)
        final_list.append(x)
        final_dict[f'elem_{num}'] = x
    print(final_list)
    print(final_dict)


if __name__ == "__main__":
    generate(1, 10)
