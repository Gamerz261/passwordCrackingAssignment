# MD5: Encrypt and decrypt
import hashlib
from hashlib import md5

class MD5:
    def __init__(self, data = "5a8dd3ad0756a93ded72b823b19dd877"):
        self.data = data
    def encrypt(self):
        self.data = md5(self.data.encode()).hexdigest()
        return "Crypted: "+self.data
    def decrypt(self, data):
        if md5(data.encode()).hexdigest() == self.data:
            return "Decrypted: "+data
            del self.data
        else:
            return "Error"

#crypt = MD5()
#print(crypt.encrypt()) # Encrypt
#print(crypt.decrypt("5a8dd3ad0756a93ded72b823b19dd877")) # Decrypt data argument