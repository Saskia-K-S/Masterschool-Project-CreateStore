import sys
from store import Store
from products import Product

MENU = """
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""


def list_all_products(store: Store):
    list_of_active_products = store.get_all_products()
    if not list_of_active_products:
        print("Currently, all products are sold out.")
    else:
        for index, product in enumerate(list_of_active_products):
            print(f"{index + 1}. {product.show()}")


def show_amount_in_store(store: Store):
    total_quantity = store.get_total_quantity()
    print(f"There is a total quantity of {total_quantity} in the store currently.")


def make_an_order(store: Store):
    products = store.get_all_products()
    print(len(products))
    shopping_cart = []
    list_all_products(store)
    print("When you want to finish order, enter empty text.")
    while True:
        product_choice = input("Which product # do you want? ")
        quantity_choice = input("What amount do you want? ")

        # if int(product_choice) > len(products) or int(product_choice) < 1:
        #    raise ValueError("Invalid product choice.")
        if product_choice == "" or quantity_choice == "":
            break
        if int(product_choice) > len(products) or int(product_choice) < 1:
            print("Error adding product.")
            break
        else:
            product = products[int(product_choice) - 1]
            if int(quantity_choice) > product.get_quantity() or int(quantity_choice) <= 0:
                print("Error adding the product.")
                break
            shopping_cart.append((product, int(quantity_choice)))
            print("Product added to list!")

    total_price_of_order = store.order(shopping_cart)
    print("*" * 42)
    print(f"Order made! Total payment of the order is: {total_price_of_order}$.")


# needs work
def quit():
    sys.exit()


def call_function(func, *args):
    func(*args)


def start(store: Store):
    menu_dictionary = {
        "1": (list_all_products, store),
        "2": (show_amount_in_store, store),
        "3": (make_an_order, store),
        "4": (quit,)
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
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


main()
