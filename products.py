import store
from typing import Optional
from promotion import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount
"""
Product Class.
"""


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
        self.promotion = Optional[Promotion]

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
        return f"Product name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promotion}."

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.
        :param quantity: Instance of Class Product.
        """
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
        :param quantity: Instance of class Product.
        :return: total_price
        """
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity is not an integer. Found {type(quantity).__name__}")
        if quantity <= 0:
            raise ValueError("Quantity needs to be greater than zero.")
        if self.quantity < quantity:
            raise ValueError("The chosen number of the product is currently not in stock.")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)

        return total_price

    def set_promotion(self, promotion):
        set_promotion = promotion

    def get_promotion(self, promotion):
        return self.promotion


"""
NonStockedProduct Class.
"""


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        return f"Non stocked product name: {self.name}, Price: {self.price}, Quantity: is not applicable, Promotion: {self.promotion}."


"""
LimitedProduct
"""


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"The quantity cannot exceed the available quantity of {self.maximum}.")

        return super().buy(quantity)

    def show(self):
        return (f"Limited product: {self.name}, Price: {self.price}, Maximal purchase quantity: {self.maximum}, "
                f"Promotion: {self.promotion}.")


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=100, maximum=1),
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)


if __name__ == "__main__":
    main()