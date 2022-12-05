# MD5: Encrypt and decrypt
import hashlib, time, itertools
from hashlib import md5
from multiprocessing import Process, current_process
# Import libraries from the dictionary attack file
from Methods.dictionaryAttack import DictionaryAttack


# au
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

    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    previous = ''
    charCol = 0

    start = time.time()
    distance = ""
    attempts = 0
    cracked = False

    def __init__(self, user):
        # Initialize variable
        self.data = user

    def encrypt(self):
        self.data = md5(self.data.encode()).hexdigest()
        return self.data

    def bruteDecrypt(self, input):  # this fr just took 14 minutes on a random 5 digit password but it works i guess
        # print(self.blue + "Beginning brute force cracking... This may take a while.")
        # for i in range(1, 9):
        #     for letter in itertools.product(self.chars, repeat=i):
        self.attempts += 1
        letter = input
        letterHash = hashlib.sha256(letter.encode('utf-8')).hexdigest()

        if letterHash.rstrip() == self.data.rstrip():
            self.distance = time.time() - self.start
            print(self.pink + "Password found through brute force in " + str(self.distance) + " seconds and " + str(
                self.attempts) + " attempts!")
            print(self.green + "Password: " + self.white + letter)
            return

    def multiThread(self):
        # worker_count = 40320
        worker_pool = []
        while not self.cracked:
            newPassword = ''
            # Reset the password to the initial character if col is maxed
            if self.charCol > len(self.chars):
                newPassword = '1'
                for _ in self.charCol:
                    newPassword = newPassword + '1'
                self.charCol = 1
            elif self.previous == '':
                newPassword = '1'
            else:
                newPassword = self.previous[:len(self.previous - 1)] + self.chars[self.charCol]
            self.previous = newPassword
            p = Process(self.bruteDecrypt(newPassword))
            p.start()
            worker_pool.append(p)
        for p in worker_pool:
            p.join()  # Wait for all of the workers to finish.

    def decrypt(self):
        # Output Variables
        password = ''
        hashword = ''
        start = time.time()
        distance = ""
        attempts = 0
        for count in range(10000):
            attempts += 1
            password = DictionaryAttack.list(self, count).rstrip()
            hashword = hashlib.md5(password.encode('utf-8')).hexdigest()
            cracked = False
            if hashword == self.data:
                distance = time.time() - start
                cracked = True
                break
        if cracked:
            print(self.pink + "Password found in " + str(distance) + " seconds and " + str(attempts) + " attempts!")
            print(self.green + "Password:", end=' ')
            print(self.white + password)
            print(self.green + "MD5 Hash:", end=' ')
            print(self.white + hashword)
        else:
            print(self.red + "That password is not in the top 10,000 passwords.")
            user = input(self.blue + "Would you like to attempt to crack the password through brute force? [y/n]: ")
            if user == 'y':
                self.bruteDecrypt()
            else:
                return

# Experimental
# crypt = MD5("Hello, world!")
# print(crypt.encrypt())
# print(crypt.decrypt("Hello, world!"))
