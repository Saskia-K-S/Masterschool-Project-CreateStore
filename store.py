from products import Product
from typing import List
"""
Class Store
"""
class Store:
    def __init__(self, list_of_products):
        """
        Takes list of products as an argument. Checks if list is instance of List_of_products.
        Sets product instance variable.
        :param list_of_products: Instance of class Store.
        """
        if not isinstance(list_of_products, list):
            raise TypeError("List of products should be of type list.")
        for product in list_of_products:
            if not isinstance(product, Product):
                raise TypeError("Product needs to me an instance of class Product.")

        self.products = list_of_products  # need to find unique products from the list

    def add_product(self, product):
        """
        Function to add product.
        :param product: instance of class Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected an object of the Product class. Error.")

        if product in self.products:
            product.set_quantity(product.get_quantity() + 1)
        else:
            self.products.append(product)

    def remove_product(self, product):
        """
        Function to remove product from the store.
        :param product: instance of class Store.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected and object of the Product class. Error.")

        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product is currently not in store. Error.")

    def get_total_quantity(self):
        """
        Calculates the total quantity.
        :return: total_quantity
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        """
        Updates list of active products.
        :return: list_of_active_products
        """
        list_of_active_products = []
        for product in self.products:
            if product.is_active():
                list_of_active_products.append(product)

        return list_of_active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Functionality to order product and quantity.
        :param shopping_list: instance of class Product.
        :return: total_price_of_order
        """
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"The product {product.name} is currently not available in store.")
            if not product.is_active():
                raise ValueError(f"The product {product.name} is currently not active.")
        total_price_of_order = 0
        for product, quantity in shopping_list:
            total_price_of_order += product.buy(quantity)

        return total_price_of_order
