class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.active = True

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_quantity(self):
        return float(self.quantity)

    def show(self):
        # MacBook Air M2, Price: 1450, Quantity: 100"
        return f"Product name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def set_quantity(self, quantity):
        self.quantity = quantity
        # todo: deactivate product if quantity is zero
        if quantity == 0:
            self.deactivate()

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        :param quantity:
        :return: total_price
        """

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()