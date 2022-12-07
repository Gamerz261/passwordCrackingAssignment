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
        #print('augh')
        # Encode password into a readable utf-8 byte code:
        password = self.data.encode('utf-8')

        # Hash the decoded password and generate a salt:
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashedPassword

    def decrypt(self):
        print(self.orange + "WARNING: BCrypt hashing can take several minutes!")
        # Output Variables
        password = ''
        hashword = ''
        start = time.time()
        distance = ""
        attempts = 0
        for count in range(10000):
            attempts += 1
            password = DictionaryAttack.list(self, count).rstrip()
            cracked = False
            if bcrypt.checkpw(password.encode('utf-8'), self.data.encode('utf-8')):
                distance = time.time() - start
                cracked = True
                break
        if cracked:
            print(self.pink + "Password found in " + str(distance) + " seconds and " + str(attempts) + " attempts!")
            print(self.green + "Password:", end=' ')
            print(self.white + password)
            print(self.green + "BCrypt Hash:", end=' ')
            print(self.white + str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))[2:-1])
        else:
            print(self.red + "That password is not in the top 10000 passwords.")