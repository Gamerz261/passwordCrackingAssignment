class DictionaryAttack:

    content = ""
    

    def __init__(self):
        print('Running Dictionary Attack')

    def dictSize(self):
        with open(r"bigDict.txt", 'r') as pg:
            self.content = pg.readlines()
            dictSize = len(self.content)
        #print(self.content)
        return dictSize

    def check(self, password):
        size = DictionaryAttack.dictSize(self)
        if password in self.content:
            print("Password found in the top " + str(size) + " most common passwords!")
        else:
            print("That password is not in the top " + str(size) + " passwords.")

    def list(self, index):
        return self.content[index].strip()
