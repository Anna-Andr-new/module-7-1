from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_product = file.read()
        file.close()
        return file_product

    def add(self, *products):
        for i in products:
            self.new_product = open(self.__file_name, 'r')
            if i.name not in self.new_product.read():
                self.new_product = open(self.__file_name, 'a')
                self.new_product.writelines(f'{i}\n')
                self.new_product.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине.')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
