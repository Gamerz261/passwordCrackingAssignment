import hashlib
from Methods.dictionaryAttack import DictionaryAttack
from hashlib import sha256

class SHA256:

    global userIn
    userIn = ''

    def encrypt(self,runner):
        userIn = runner
        hashedInput = hashlib.sha256(userIn.encode('utf-8')).hexdigest()
        return hashedInput
    def decrypt(self):
        print(userIn)
        hashed = SHA256.encrypt(self)
        content = ''
        content1 = ''
        for count in range(10000):
            content = DictionaryAttack.list(self ,count).rstrip()
            content1 = hashlib.sha256(content.encode('utf-8')).hexdigest()
            cracked = False
            if content1 == hashed:
                cracked = True
                break
        if cracked:
            print("Password Found! \nPassword: " + content + "\nSHA256 Hash: " + content1)
        else:
            print("That password is not in the top 10000 passwords.")

