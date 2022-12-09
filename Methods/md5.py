# MD5: Encrypt and decrypt
import hashlib,time, itertools
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
    
    # List all of the characters use for decryption (Base96)
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    
    # Analysis data
    start = time.time()
    distance = ""
    attempts = 0
    cracked = False
    
    def __init__(self, user):
        # Initialize variable
        self.data = user
    
    # Encrypt!
    def encrypt(self):
        # Use the md5 Library to convert data to utf-8 and then uncode using md5 library
        self.data = md5(self.data.encode()).hexdigest()
        return self.data
    
    # Called by self.decrypt
    def bruteDecrypt(self):
        print(self.blue + "Beginning brute force cracking... This may take a while.")
        # itterate through every 8 character password beginning with "1" and going through self.chars
        for i in range(1, 9):
            for letter in itertools.product(self.chars, repeat=i):
                self.attempts += 1
                letter = ''.join(letter)
                letterHash = md5(letter.encode('utf-8')).hexdigest()

                if letterHash.rstrip() == self.data.rstrip():
                    self.distance = time.time() - self.start
                    print(self.pink + "Password found through brute force in " + str(self.distance)+ " seconds and "+ str(self.attempts) + " attempts!")
                    print(self.green + "Password: " + self.white + letter)
                    return

    def decrypt(self):
        # Output Variables
        password = ''
        hashword = ''
        
        # Start the time function for analysis
        start = time.time()
        distance = ""
        attempts = 0
        
        # Pull the size of the dictionary from the DictionaryAttack method
        dictSize = DictionaryAttack.dictSize(self)
        
        # Itterate through the dictionary
        for count in range(dictSize):
            attempts += 1
            
            password = DictionaryAttack.list(self, count).rstrip()
            # Encode each dictionary entity
            hashword = hashlib.md5(password.encode('utf-8')).hexdigest()
            cracked = False
            
            # Compare the hashes from the dictionary to the input
            if hashword == self.data:
                distance = time.time() - start
                cracked = True
                break
        # If the hash matched the input, print the outcome to the command line
        if cracked:
            print(self.pink + "Password found in " + str(distance) + " seconds and " + str(attempts) + " attempts!")
            print(self.green + "Password:" + self.white + password)
            print(self.green + "MD5 Hash:" + self.white + hashword)
        # If the hash DID NOT match any of the hashes from the dictionary, prompt the user with the option to brute force the password
        else:
            print(self.red + "That password is not in the top " + str(dictSize) + " passwords.")
            user = input(self.blue + "Would you like to attempt to crack the password through brute force? [y/n]: ")
            
            # If the user selects y, call the brute force method (self.bruteDecrypt)
            if user == 'y':
                self.bruteDecrypt()
            else:
                return
