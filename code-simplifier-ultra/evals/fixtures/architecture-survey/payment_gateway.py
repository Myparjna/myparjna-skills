def charge(gateway, amount):
    return gateway.charge(amount, idempotent=True)
