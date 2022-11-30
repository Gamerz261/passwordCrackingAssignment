# MD5: Encrypt and decrypt
import hashlib,time
from hashlib import md5
# Import libraries from the dictionary attack file
from Methods.dictionaryAttack import DictionaryAttack


class MD5:
    # Define storage for hash
    data = ''

    # CoLoR cOdEs
    white = "\033[38;5;252m"
    pink = "\033[38;5;5m"
    red = "\033[38;5;1m"
    orange = "\033[38;5;3m"
    green = "\033[38;5;150m"
    blue = "\033[38;5;4m"
    purple = "\033[38;5;20m"

    def __init__(self, user):
        # Initialize variable
        self.data = user

    def encrypt(self):
        self.data = md5(self.data.encode()).hexdigest()
        return self.data

    def decrypt(self):
        # Output Variables
        password = ''
        hashword = ''
        start = time.time()
        distance = ""
        attempts = 0
        for count in range(10000):
            attempts += 1
            password = DictionaryAttack.list(self, count).rstrip()
            hashword = hashlib.md5(password.encode('utf-8')).hexdigest()
            cracked = False
            if hashword == self.data:
                distance = time.time() - start
                cracked = True
                break
        if cracked:
            print(self.pink + "Password found in " + str(distance) + " seconds and " + str(attempts) + " attempts!")
            print(self.green + "Password:", end=' ')
            print(self.white + password)
            print(self.green + "MD5 Hash:", end=' ')
            print(self.white + hashword)
        else:
            print(self.red + "That password is not in the top 10000 passwords.")

# Experimental
# crypt = MD5("Hello, world!")
# print(crypt.encrypt())
# print(crypt.decrypt("Hello, world!"))
