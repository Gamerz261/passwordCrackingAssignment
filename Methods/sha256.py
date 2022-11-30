import hashlib, multiprocessing, time
from Methods.dictionaryAttack import DictionaryAttack
from hashlib import sha256


class SHA256:

    def encrypt(self,runner):
        hashedInput = hashlib.sha256(runner.encode('utf-8')).hexdigest()
        return hashedInput

    def decrypt(self, runner):
        userIn = runner
        password = ''
        hashword = ''
        start = time.time()
        distance = ""

        white = "\033[38;5;252m"
        pink = "\033[38;5;5m"
        red = "\033[38;5;1m"
        orange = "\033[38;5;3m"
        green = "\033[38;5;150m"
        blue = "\033[38;5;4m"
        purple = "\033[38;5;20m"
        attempts = 0
        for count in range(10000):
            attempts+=1
            password = DictionaryAttack.list(self ,count).rstrip()
            hashword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            cracked = False
            if hashword == userIn:
                distance = time.time() - start
                cracked = True
                break
        if cracked:
            print(pink + "Password found in " + str(distance) + " seconds and "+ str(attempts) + " attempts!")
            print(green + "Password:",end = ' ')
            print(white + password)
            print(green + "SHA256 Hash:",end = ' ')
            print(white + hashword)
            
        else:
            print("That password is not in the top 10000 passwords.")