from products import Product
from typing import List, Tuple


class Store:
    def __init__(self, list_of_products):
        self.products = list_of_products  # need to find unique products from the list

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Expected and object of the Product class. Error.")

        if product in self.products:
            product.set_quantity(product.get_quantity() + 1)
        else:
            self.products.append(product)

    def remove_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Expected and object of the Product class. Error.")

        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product is currently not in store. Error.")

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        list_of_active_products = []
        for product in self.products:
            if product.is_active():
                list_of_active_products.append(product)

        return list_of_active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price_of_order = 0
        for product, quantity in shopping_list:
            total_price_of_order += product.buy(quantity)

        return total_price_of_order


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
