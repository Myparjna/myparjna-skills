def discount(user, total):
    if user is not None:
        if user.get("member"):
            if total > 100:
                return total * 0.1
    return 0
