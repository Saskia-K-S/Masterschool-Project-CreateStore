import sys

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
        self.promotion: Optional[Promotion] = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f"The name should be a string.")
        if not name.strip():
            raise ValueError(f"Invalid name - empty name is not applicable.")
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError(f"The price needs to be a number.")
        if price < 0:
            raise ValueError(f"Price needs to be greater than zero.")
        self._price = price

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        if not isinstance(active, bool):
            raise TypeError(f"Active needs to be of type boolean.")
        self._active = active

    def is_active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    @property
    def quantity(self):
        return int(self._quantity)

    def __str__(self):
        # MacBook Air M2, Price: 1450, Quantity: 100"
        promotion_info = f"Promotion: {self.promotion.promotion_name}" if self.promotion else "No promotion"
        return f"Product name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}."

    def __repr__(self):
        return (
            f"{type(self).__name__}, (Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, "
            f"Active: {self.active}, Promo: {repr(self.promotion)})"
        )

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of the product.
        :param quantity: Instance of Class Product.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity should be of type integer.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if quantity == 0:
            self.deactivate()

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        if promotion is not None and not isinstance(promotion, Promotion):
            raise TypeError(f"Expected promotion should be an instance of Promotion.")
        self._promotion = promotion

    def __lt__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"Expected a product for comparison.")
        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"Expected a product for comparison.")
        return self.price > other.price

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

        self.quantity = self.quantity - quantity

        return total_price

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion


"""
NonStockedProduct Class.
"""


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=sys.maxsize)

    @property
    def quantity(self):
        """Unlimited quantity available." """
        return "Unlimited quantity available."  #sys.maxsize

    @quantity.setter
    def quantity(self, quantity):
        if quantity != sys.maxsize:
            raise ValueError(f"Cannot set quantity for non-stocked products.")
        self._quantity = quantity

    def buy(self, quantity):
        if not self.is_active():
            raise TypeError(f"Product {self.name} is not active.")
        if self.promotion is None:
            total_price = self.price * quantity
        else:
            total_price = self.promotion.apply_promotion(self, quantity)
        return total_price

    def __str__(self):
        promotion_info = f"Promotion: {self.promotion.promotion_name}" if self.promotion else "No promotion"
        return f"Non stocked product name: {self.name}, Price: {self.price}, Quantity: is not applicable, {promotion_info}."


"""
LimitedProduct
"""


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        if not isinstance(maximum, int):
            raise TypeError("Maximum needs to be of type integer.")
        if maximum < 0:
            raise ValueError(f"Negative numbers are not acceptable.")
        self._maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"The quantity cannot exceed the available quantity of {self.maximum}.")

        return super().buy(quantity)

    def __str__(self):
        promotion_info = f"Promotion: {self.promotion.promotion_name}" if self.promotion else "No promotion"
        return (f"Limited product: {self.name}, Price: {self.price}, Maximal purchase quantity: {self.maximum}, "
                f"{promotion_info}.")
