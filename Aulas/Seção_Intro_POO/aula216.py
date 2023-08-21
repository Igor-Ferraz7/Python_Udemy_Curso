# Agregação: POSSUIR/TER um objeto (ou seja, ele o salva)
class Cart:
    def __init__(self) -> None:
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])
    

    def insert_products(self, *products): # Observando que adicionam objetos numa tupla (tem q desempacotar com for)
        # self._products += products
        for product in products:
            self._products.append(product)


    def list_products(self):
        for product in self._products:
            print(f"Product: {product.name}, Price: {product.price}")


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


c1 = Cart()
p1, p2 = Product("Milk", 10.99), Product("Cereal", 13.99)
c1.insert_products(p1, p2)
c1.list_products()
