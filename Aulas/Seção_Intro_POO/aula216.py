class Cart:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, *product):
        print(product) # Observando que adicionam objetos numa tupla (tem q desempacotar com for)
        self.products.append(product)
    
    # def show_products(self):
        # for product in self.products:
            # print(product.name, product.price)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart1 = Cart()
pen = Product('Pen', 1.5)
pencil = Product('Pencil', 2.0)
cart1.add_product(pen, pencil)
# cart1.show_products()


