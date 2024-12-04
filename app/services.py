import secrets


def generate_pin():
    return secrets.randbelow(900000) + 100000
