class Product:
    def __init__(self, name, volume):
        self.name = name
        self.volume = round(volume, 2)


class Warehouse:
    def __init__(self, max_stock):
        self.max_stock = max_stock
        self.items = []

    def add(self, product):
        if self.get_current_stock() + product.volume > self.max_stock:
            return -1
        else:
            self.items.append(product)

    def get_current_stock(self):
        return round(sum([item.volume for item in self.items]), 2)
