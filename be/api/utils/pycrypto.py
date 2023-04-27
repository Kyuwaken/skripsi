import base64, json 
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

# key = '6c33d4abde09fe1c4ac9b76f245d7df4'
# iv = 'ddc5b6c4d6e4b6c4'
# def encrypt_data(data):
#         data= pad(data.encode(),16)
#         cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv.encode('utf-8'))
#         return base64.b64encode(cipher.encrypt(data)).decode("utf-8", "ignore")

def decrypt_data(enc):
        enc = enc.encode("utf-8", "ignore")
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc),16)

def decrypt_data_fe(enc):
        enc = enc.encode("utf-8", "ignore")
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        data = unpad(cipher.decrypt(enc),16).decode()
        return json.loads(data)

# def decrypt_data_fe(enc):
#         breakpoint()
#         cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
#         decoded_data = base64.b64decode(enc)
#         decrypted_data = unpad(cipher.decrypt(decoded_data),16)
#         # cipher.decrypt(decoded_data).decode('utf-8').rstrip('\0')
#         return decrypted_data
# def decrypt_data_fe(enc):
#     enc = base64.b64decode(enc)
#     cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
#     decrypted = cipher.decrypt(enc)
#     data= unpad(decrypted, 16).decode('utf-8')
#     return json.loads(data)

# def decrypt_data_fe(enc):
#         breakpoint()
#         enc = enc.encode("utf-8", "ignore")
#         enc = base64.b64decode(enc)
#         cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
#         # decrypted = unpad(cipher.decrypt(enc),16)
#         decrypted_bytes = cipher.decrypt(enc)
#         decrypted_text = decrypted_bytes.decode('utf-8').rstrip('\0')
#         return json.loads(decrypted_text)

# encrypted = encrypt_data(data)
# print('encrypted ECB Base64:',encrypted.decode("utf-8", "ignore"))

# decrypted = decrypt_data(encrypted)
# print('data: ',decrypted.decode("utf-8", "ignore"))