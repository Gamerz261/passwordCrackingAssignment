import bcrypt

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

    def __int__(self, user):
        self.data = user

    def encrypt(self):
        #print('augh')
        # Encode password into a readable utf-8 byte code:
        password = self.data.encode('utf-8')

        # Hash the decoded password and generate a salt:
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashedPassword

    def decrypt(self):
        print('augh v2')