import secrets


def generate_pin():
    return secrets.randbelow(900000) + 100000


def send_otp_email(email, pin):
    pass
