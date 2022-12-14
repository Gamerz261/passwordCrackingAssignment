import hashlib
import time
from multiprocessing import Process
from basehash import base94
from Methods.dictionaryAttack import DictionaryAttack


class SHA256:
    white = "\033[38;5;252m"
    pink = "\033[38;5;5m"
    red = "\033[38;5;1m"
    orange = "\033[38;5;3m"
    green = "\033[38;5;150m"
    blue = "\033[38;5;4m"
    purple = "\033[38;5;20m"

    password = ''
    hashword = ''

    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    previous = ''
    base94 = base94()
    charCol = 1

    start = time.time()
    distance = ""
    attempts = 0
    cracked = False

    def __init__(self, user):
        self.data = user

    def encrypt(self):
        self.data = hashlib.sha256(self.data.encode('utf-8')).hexdigest()
        return self.data

    def bruteDecrypt(self):  # this fr just took 14 minutes on a random 5 digit password but it works i guess
        while not self.cracked:
            # print(self.blue + "Beginning brute force cracking... This may take a while.")
            # for i in range(1, 9):
            #     for letter in itertools.product(self.chars, repeat=i):
            self.attempts += 1
            letter = self.base94.encode(self.charCol)
            # print("BDC - " + letter)
            self.charCol += 1
            self.previous = letter
            letterHash = hashlib.sha256(letter.encode('utf-8')).hexdigest()

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
        print(self.blue + "Multithreading brute force cracking... This may take a while.")
        worker_count = 128
        global worker_pool
        worker_pool = []
        for _ in range(worker_count):
            p = Process(target=self.bruteDecrypt(), args=())
            p.start()
            worker_pool.append(p)
        for p in worker_pool:
            p.join()  # Wait for all of the workers to finish.

    def dictDecrypt(self):
        dictSize = DictionaryAttack.dictSize(self)
        for count in range(dictSize):
            self.attempts += 1
            self.password = DictionaryAttack.list(self, count)
            self.hashword = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
            if self.hashword == self.data:
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
                self.multiThread()
            else:
                return
