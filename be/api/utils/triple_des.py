from Crypto.Cipher import DES3


class TripleDES:

    def __init__(self, key):
        if isinstance(key, bytes) or isinstance(key, bytearray):
            self.key = DES3.adjust_key_parity(key)
        else:
            self.key = DES3.adjust_key_parity(bytearray(key, 'utf-8'))

        self.cipher = DES3.new(key, DES3.MODE_ECB)

    def encrypt(self, plain_text):
        plain_text = self.zero_pad(plain_text)
        encrypted_msg = self.cipher.encrypt(plain_text)
        result = ''
        for x in encrypted_msg:
            temp = hex(x)[2:]
            if len(temp) == 1:
                temp = "0" + temp
            result += temp

        return result

    @staticmethod
    def zero_pad(data):
        if not isinstance(data, bytes) and not isinstance(data, bytearray):
            data = bytearray(data, 'utf-8')

        n = len(data)
        if n % 8 != 0:
            for x in range(8 - (n % 8)):
                data.append(0)

        return data
