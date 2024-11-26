from products import Product
import pytest


def test_creating_product():
    product = Product("Game boy color", price=30, quantity=1)
    # assertion
    assert product.name == "Game boy color"
    assert product.price == 30
    assert product.quantity == 1


def test_create_product_invalid():
    # Empty name
    with pytest.raises(ValueError, match="Invalid name or string. Empty string cannot be accepted as a name."):
        Product("", 1450, 100)

    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=10, quantity=-100)


def test_becomes_inactive():
    product = Product("Game boy color", price=30, quantity=1)
    product.quantity(0)

    assert product.is_active() is False


def test_modify_right_output():
    product = Product("Game boy color", price=30, quantity=10)
    total_price = product.buy(5)

    assert total_price == 150
    assert product.quantity() == 5
    assert product.is_active() is True


def test_invoke_exception():
    product = Product("Nintendo 64", price=50, quantity=1)
    with pytest.raises(ValueError, match="The chosen number of the product is currently not in stock."):
        product.buy(5)




