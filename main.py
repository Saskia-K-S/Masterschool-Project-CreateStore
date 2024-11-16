import sys
from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotion import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount

import promotion

MENU = """
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""


def list_all_products(store: Store):
    """
    Lists all active products.
    :param store: An instance of Store.
    """
    list_of_active_products = store.get_all_products()
    if not list_of_active_products:
        print("Currently, all products are sold out.")
    else:
        for index, product in enumerate(list_of_active_products):
            print(f"{index + 1}. {product.show()}")


def show_amount_in_store(store: Store):
    """
    Displays the current active quantity of products in Store.
    :param store: Instance of Store.
    """
    total_quantity = store.get_total_quantity()
    print(f"There is a total quantity of {total_quantity} in the store currently.")


def make_an_order(store: Store):
    """
    User input management; Oder products and quantity; Error handling, such as
    - Ordering a quantity too large
    - Product that runs out of stock
    - Products that is created with invalid parameters
    :param store: Instance of Store.
    """
    products = store.get_all_products()
    shopping_cart = []
    list_all_products(store)
    print("When you want to finish order, enter empty text.")
    while True:
        product_choice = input("Which product # do you want? ")
        quantity_choice = input("What amount do you want? ")

        if product_choice == "" or quantity_choice == "":
            break
        try:
            product_index = int(product_choice)-1
            quantity = int(quantity_choice)
            if product_index >= len(products) or product_index < 0:
                print("Error adding product. Please make a valid product choice.")
                continue
            product = products[product_index]
            if quantity > product.get_quantity() or quantity <= 0:
                print("Error adding the product due to invalid quantity.")
                continue

            shopping_cart.append((product, quantity))
            print("Product added to list!")
        except ValueError as v:
            print(f"Please enter valid numeric value. An error occurred: {v}")

    total_price_of_order = store.order(shopping_cart)
    print("*" * 42)
    print(f"Order made! Total payment of the order is: {total_price_of_order}$.")


def quit_shopping():
    """
    Used to quit the shopping process.
    """
    sys.exit()


def call_function(func, *args):
    """
    Calls functions with the given arguments. Used for user choice menu.
    :param func: function.
    :param args: given arguments from menu_dictionary.
    """
    func(*args)


def start(store: Store):
    """
    Displays the menu for user choice using a dispatcher pattern and starts the shopping store.
    :param store: Instance of Store.
    :return: user choice menu.
    """
    menu_dictionary = {
        "1": (list_all_products, store),
        "2": (show_amount_in_store, store),
        "3": (make_an_order, store),
        "4": (quit_shopping,)
    }
    while True:
        print(MENU)
        user_choice = input("Please enter a number from the menu: ")
        if user_choice in menu_dictionary:
            call_function(*menu_dictionary[user_choice])


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
    thirty_percent = PercentDiscount("30% off!", percent_value=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()