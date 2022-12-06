# MD5: Encrypt and decrypt
import hashlib
import time
from hashlib import md5
from multiprocessing import Process
from basehash import base94
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

    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    previous = ''
    base94 = base94()
    charCol = 1

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

    def bruteDecrypt(self):  # this fr just took 14 minutes on a random 5 digit password but it works i guess
        # print(self.blue + "Beginning brute force cracking... This may take a while.")
        # for i in range(1, 9):
        #     for letter in itertools.product(self.chars, repeat=i):
        # print("BDC - " + input)
        while not self.cracked:

            self.attempts += 1
            letter = self.base94.encode(self.charCol)
            #print("BDC - " + letter)
            self.charCol += 1
            self.previous = letter
            letterHash = hashlib.md5(letter.encode('utf-8')).hexdigest()

            if letterHash.rstrip() == self.data.rstrip():
                self.cracked = True
                self.distance = time.time() - self.start
                print(self.pink + "Password found through brute force in " + str(self.distance) + " seconds and " + str(
                    self.attempts) + " attempts!")
                print(self.green + "Password: " + self.white + letter)
                self.killWorkers()
                return

    def killWorkers(self):
        for p in worker_pool:
            p.terminate()
        return

    def multiThread(self):
        worker_count = 128
        global worker_pool
        worker_pool = []
        for _ in range(worker_count):
            p = Process(target=self.bruteDecrypt(), args=())
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
            d = DictionaryAttack()
            password = d.list(count).rstrip()
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
                self.multiThread()
            else:
                return

# Experimental
# crypt = MD5("Hello, world!")
# print(crypt.encrypt())
# print(crypt.decrypt("Hello, world!"))
