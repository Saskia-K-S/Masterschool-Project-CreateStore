from products import Product, NonStockedProduct, LimitedProduct
from typing import List, Tuple

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
        self.products = list_of_products  # need to find unique products from the list

    def __contains__(self, item):
        return item in self.products

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, list_of_products):
        if not isinstance(list_of_products, list):
            raise TypeError("List of products should be of type list.")
        for product in list_of_products:
            if not isinstance(product, (Product, NonStockedProduct, LimitedProduct)):
                raise TypeError("Product needs to be an instance of class Product.")
        self._products = list_of_products

    def add_product(self, product):
        """
        Function to add product.
        :param product: instance of class Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected an object of the Product class. Error.")
        if product in self.products:
            product.quantity(product.quantity() + 1)
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
            if isinstance(product.quantity, int):
                total_quantity += product.quantity

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

    def __add__(self, other):
        """
        Overwrites the product in store class
        create new instance from store
        :param other:
        :return:
        """
        if not isinstance(other, Store):
            raise TypeError(f"Unsupported operants for + operator.")
        products = []
        for product in self.products:
            if isinstance(product.quantity, int):
                additional_quantity = 0
                for other_product in other.products:
                    if (isinstance(other_product, Product) and
                            other_product.name == product.name and
                            other_product.price == product.price and
                            other_product.active == product.active and
                            other_product.promotion == product.promotion):
                        additional_quantity += other_product.quantity

                product.quantity += additional_quantity
            products.append(product)
        for product in other.products:
            is_in_self_products = False
            for prod in self.products:
                if (type(prod) is type(product) and
                        prod.name == product.name and
                        prod.price == product.price and
                        prod.active == product.active and
                        prod.promotion == product.promotion
                ):
                    is_in_self_products = True
                    break
            if not is_in_self_products:
                products.append(product)
        return Store(products)

    def __repr__(self):
        product_reprs = []
        for prod in self.products:
            product_reprs.append(repr(prod))

        return f"{type(self).__name__}({product_reprs})"
