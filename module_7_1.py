class Shop:
    def __init__(self):
        self.file_name = 'products.txt'
    def get_products(self):
        file = open(self.file_name, 'r')
        products = file.read()
        file.close()
        return products
    def add(self,*products):
        cp = self.get_products()
        file = open(self.file_name, 'a')
        for product in products:
            if str(product) not in cp:
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product} уже есть в магазине')
        file.close()


class Product:
    def __init__(self,name,weigth,category):
        self.name = name
        self.weigth = weigth
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigth}, {self.category}'

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())