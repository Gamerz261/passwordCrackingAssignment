import hashlib
from hashlib import sha256

class SHA256:
    global userIn
    userIn = ''
    hashedInput = ''

    def __init__(self, runner):
        userIn = runner

    def decrypt(self):
        
        hashedInput = hashlib.sha256(userIn.encode('utf-8'))
        #print ("what" + str(hashedInput))
        print("wha")
        print(userIn)
        print(hashedInput)
        InputFile = open(r"passList.txt","r")
        content = InputFile.readlines()
        count = 0;
        for line in content:
            count +=1 
            #print(line)
            #print(hashlib.sha256(line.encode('utf-8')))
            if (hashedInput == hashlib.sha256(line.encode('utf-8'))):
                print("Password found:")
        InputFile.close()