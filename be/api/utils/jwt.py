import jwt

from datetime import timedelta
from django.conf import settings
from django.utils import timezone

def generate_token(id, username, name, role):
    payload = {
        "id": id,
        "username": username,
        "name": name,
        "role": role
    }
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def decode_token(encoded_jwt):
    try:
        return jwt.decode(encoded_jwt, settings.SECRET_KEY, algorithms=["HS256"])
    except Exception:
        return None
