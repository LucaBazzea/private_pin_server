import secrets

from django.conf import settings

import requests

import boto3
from botocore.exceptions import ClientError


def generate_pin():
    return secrets.randbelow(900000) + 100000


def send_otp_email(email, pin):
    ses = boto3.client(
        "ses",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

    message = {
        "Source": "no-reply@privatepin.app",
        "Destination": {
            "ToAddresses": [email],
            "CcAddresses": [],
            "BccAddresses": []
        },
        "Message": {
            "Body": {
                "Text": {
                    "Data": f"Your OTP is: {pin}"
                }
            },
            "Subject": {
                "Data": "PrivatePin OTP"
            }
        }
    }

    try:
        response = ses.send_email(Message=message)
        print("Email sent successfully!")
        print(response)
    except ClientError as e:
        print("Error sending email:", e.response["Error"]["Message"])

def generate_username(email):
    return email.split("@")[0] + str(secrets.randbelow(9000) + 1000)
