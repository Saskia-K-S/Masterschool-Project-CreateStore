class Product:
    def __init__(self, name, price, quantity):

        if not isinstance(name, str):
            raise TypeError("Name should be a string.")
        if not name.strip():
            raise ValueError("Invalid name or string. Empty string cannot be accepted as a name.")
        if not isinstance(price, (float, int)):
            raise TypeError("Price should be of type float or integer.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity should be of type integer.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

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
        if not isinstance(quantity, int):
            raise TypeError("Quantity should be of type integer.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        :param quantity:
        :return: total_price
        """
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity is not an integer. Found {type(quantity).__name__}")
        if quantity <= 0:
            raise ValueError("Quantity needs to be greater than zero.")
        if self.quantity < quantity:
            raise ValueError("The chosen number of the product is currently not in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_price
