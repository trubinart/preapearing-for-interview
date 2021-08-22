class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.name} - {self.price}')


if __name__ == '__main__':
    a = ItemDiscount('нож', 500)
    b = ItemDiscountReport('пила', 400)
    b.get_parent_data()
