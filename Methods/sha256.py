import hashlib, multiprocessing, time
from Methods.dictionaryAttack import DictionaryAttack
from hashlib import sha256


class SHA256:

    white = "\033[38;5;252m"
    pink = "\033[38;5;5m"
    red = "\033[38;5;1m"
    orange = "\033[38;5;3m"
    green = "\033[38;5;150m"
    blue = "\033[38;5;4m"
    purple = "\033[38;5;20m"

    def __init__(self, user):
        self.data = user

    def encrypt(self):
        hashedInput = hashlib.sha256(self.data.encode('utf-8')).hexdigest()
        return hashedInput

    def decrypt(self):
        password = ''
        hashword = ''
        start = time.time()
        distance = ""
        attempts = 0
        for count in range(10000):
            attempts+=1
            password = DictionaryAttack.list(self ,count).rstrip()
            hashword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            cracked = False
            if hashword == self.data:
                distance = time.time() - start
                cracked = True
                break
        if cracked:
            print(self.pink + "Password found in " + str(distance) + " seconds and "+ str(attempts) + " attempts!")
            print(self.green + "Password:" + self.white + password)
            print(self.green + "SHA256 Hash:" + self.white + hashword)
        else:
            print(self.red + "That password is not in the top 10000 passwords.")