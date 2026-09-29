def validate(order):
    if order["quantity"] <= 0:
        raise ValueError("quantity must be positive")
