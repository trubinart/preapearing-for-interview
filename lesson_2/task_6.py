
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
    def __init__(self, name, price, sale):
        self.sale = sale
        super().__init__(name, price)

    def get_parent_data(self):
        print (f'{self.name} - {self.price}')

    def __str__(self):
        return str(self.price * self.sale)


class Report1(ItemDiscountReport):
    def get_info(self):
        print(self.name)

class Report2(ItemDiscountReport):
    def get_info(self):
        print(self.price)


if __name__ == '__main__':
    a = ItemDiscount('нож', 500)
    b = ItemDiscountReport('пила', 400, 0.2)
    b.get_parent_data()
    b.name = 'блендер'
    b.price = 300
    b.get_parent_data()

    c = Report1('тапочки', 900, 0.2)
    d = Report2('оружие', 12000, 0.2)
    c.get_info()
    d.get_info()
