# Secure crypto.py (secure branch)
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

key = AESGCM.generate_key(bit_length=128)

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def encrypt_user_data(username, password):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    data = f"{username}:{password}".encode()
    ct = aesgcm.encrypt(nonce, data, None)
    return base64.b64encode(nonce + ct).decode()