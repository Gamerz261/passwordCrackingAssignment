
class DictionaryAttack:

    content = ""
    white = "\033[38;5;252m"
    pink = "\033[38;5;5m"
    red = "\033[38;5;1m"
    orange = "\033[38;5;3m"
    green = "\033[38;5;150m"
    blue = "\033[38;5;4m"
    purple = "\033[38;5;20m"
    

    def __init__(self):
        print(self.blue+"Running Dictionary Attack")

    def dictSize(self):
        with open(r"bigDict.txt", 'r') as pg:
            self.content = pg.readlines()
            dictSize = len(self.content)
        #print(self.content)
        return dictSize

    def check(self, password):
        password += "\n"
        size = DictionaryAttack.dictSize(self)
        if password in self.content:
            print(self.green+"Password found in the top " + str(size) + " most common passwords!")
            print("Password: "+ self.white + password, end='')
        else:
            print("That password is not in the top " + str(size) + " passwords.")

    def list(self, index):
        return self.content[index].strip()
