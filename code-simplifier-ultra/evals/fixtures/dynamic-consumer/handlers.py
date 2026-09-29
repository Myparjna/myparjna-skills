def legacy_receipt(record):
    return {"amount": record["cents"] / 100, "version": 1}


def current_receipt(record):
    return {"amount": record["amount"], "version": 2}
