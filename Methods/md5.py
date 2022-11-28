# MD5: Encrypt and decrypt
import hashlib
from hashlib import md5

class MD5:
    data = ''
    def __init__(self, input):
        self.data = input
    def encrypt(self):
        self.data = md5(self.data.encode()).hexdigest()
        return "Crypted: "+self.data
    def decrypt(self):
        md5(data.encode()).hexdigest()

# Experimental
# crypt = MD5("Hello, world!")
# print(crypt.encrypt())
# print(crypt.decrypt("Hello, world!"))
