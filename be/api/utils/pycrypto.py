import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from django.conf import settings

#AES ECB mode without IV

# data = 'I love Medium'
key = settings.SECRET_KEY #Must Be 16 char for AES128
iv = settings.IV.encode('utf-8')
# def encrypt_data(raw):
#         raw = pad(raw.encode(),16)
#         cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#         return base64.b64encode(cipher.encrypt(raw))

# def decrypt_data(enc):
#         enc = base64.b64decode(enc)
#         cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#         return unpad(cipher.decrypt(enc),16).decode()

def encrypt_data(data):
        data= pad(data.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        return base64.b64encode(cipher.encrypt(data)).decode("utf-8", "ignore")

def decrypt_data(enc):
        enc = enc.encode("utf-8", "ignore")
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc),16)

# encrypted = encrypt_data(data)
# print('encrypted ECB Base64:',encrypted.decode("utf-8", "ignore"))

# decrypted = decrypt_data(encrypted)
# print('data: ',decrypted.decode("utf-8", "ignore"))