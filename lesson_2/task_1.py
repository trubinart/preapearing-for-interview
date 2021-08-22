
class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.name} - {self.price}')



if __name__ == '__main__':
    a = ItemDiscount('нож', 500)
    b = ItemDiscountReport('пила', 400)
    b.get_parent_data()