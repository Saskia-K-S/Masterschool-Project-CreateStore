from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, promotion_name):
        if not isinstance(promotion_name, str):
            raise TypeError("Expected promotion name is a string.")
        if not promotion_name.strip():
            raise ValueError("Invalid promotion name - empty string is causing an error.")

        self.promotion_name = promotion_name
    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        returns the promoted price after promotion
        :param product:
        :param quantity:
        :return: promoted price after promotion
        """

    def __str__(self):
        return self.promotion_name

    def __repr__(self):
        return f"{type(self).__name__}({self.promotion_name})"


class PercentDiscount(Promotion):
    def __init__(self, promotion_name, percent_value):
        super().__init__(promotion_name)
        self.percent_value = percent_value

    def apply_promotion(self ,product ,quantity):
        discounted_price = quantity * product.price * (100 - self.percent_value)/100
        return discounted_price


class SecondHalfPrice(Promotion):
    def __init__(self, promotion_name):
        super().__init__(promotion_name)

    def apply_promotion(self, product, quantity):
        promotion_quantity = quantity//2
        non_promotion_quantity = quantity - promotion_quantity
        discounted_price = (non_promotion_quantity * product.price) + (promotion_quantity * product.price/2)
        return discounted_price


class ThirdOneFree(Promotion):
    def __init__(self, promotion_name):
        super().__init__(promotion_name)

    def apply_promotion(self, product, quantity):
        promotion_quantity = quantity//3
        non_promotion_quantity = quantity - promotion_quantity
        discounted_price = non_promotion_quantity * product.price
        return discounted_price



