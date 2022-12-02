import bcrypt, time
from Methods.dictionaryAttack import DictionaryAttack

class BCrypt:
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
        self.data = user

    def encrypt(self):
        # Encode password into a readable utf-8 byte code:
        password = self.data.encode('utf-8')

        # Hash the decoded password and generate a salt:
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashedPassword

    def dictDecrypt(self):
        dictSize = DictionaryAttack.dictSize(self)
        for count in range(dictSize):
            self.attempts += 1
            self.password = DictionaryAttack.list(self, count).rstrip()
            self.hashword = bcrypt.hashpw(self.password, bcrypt.gensalt())
            if self.hashword == self.hashedPassword:
                self.distance = time.time() - self.start
                self.cracked = True
                break
        if self.cracked:
            print(self.pink + "Password found in " + str(self.distance) + " seconds and " + str(
                self.attempts) + " attempts!")
            print(self.green + "Password:" + self.white + self.password)
            print(self.green + "SHA256 Hash:" + self.white + self.hashword)
        else:
            print(self.red + "That password is not in the top " + str(dictSize) + " passwords.")
            user = input(self.blue + "Would you like to attempt to crack the password through brute force? [y/n]: ")
            if user == 'y':
                self.bruteDecrypt()
            else:
                return


