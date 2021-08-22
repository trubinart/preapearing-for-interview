
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

    @price.setter
    def price(self, other):
        self.__price = other

    @name.setter
    def name(self, other):
        self.__name = other


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print (f'{self.name} - {self.price}')



if __name__ == '__main__':
    a = ItemDiscount('нож', 500)
    b = ItemDiscountReport('пила', 400)
    b.get_parent_data()
    b.name = 'блендер'
    b.price = 300
    b.get_parent_data()