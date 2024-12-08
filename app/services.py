import secrets


def generate_pin():
    return secrets.randbelow(900000) + 100000


def send_otp_email(email, pin):
    pass


def generate_username(email):
    return email.split("@")[0] + str(secrets.randbelow(9000) + 1000)
