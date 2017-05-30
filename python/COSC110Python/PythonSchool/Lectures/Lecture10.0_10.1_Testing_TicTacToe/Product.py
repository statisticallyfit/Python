


class Product:
    def __init__(self, quantity=0, price=0.0):
        self.stockedQuantity = quantity
        self.price = price

    def purchase(self, requiredQuantity):
        if self.stockedQuantity >= requiredQuantity:
            self.stockedQuantity -= requiredQuantity
            return requiredQuantity * self.price # returning price of the items
        # else not enough quantity
        raise ValueError("Not enough product")

