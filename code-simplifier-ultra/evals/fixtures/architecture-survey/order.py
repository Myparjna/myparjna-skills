from validate_order import validate
from price_order import price
from payment_gateway import charge


def submit(order, gateway):
    validate(order)
    return charge(gateway, price(order))
