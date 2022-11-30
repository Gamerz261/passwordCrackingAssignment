# Largely this one is just for educational purposes
# its very inefficient when you think about it (iTs VeRY inNeFFiCienT)
# Imports
import itertools
import time
class BruteForce:

    #Color codes
    white = "\033[38;5;252m"
    pink = "\033[38;5;5m"
    red = "\033[38;5;1m"
    orange = "\033[38;5;3m"
    green = "\033[38;5;150m"
    blue = "\033[38;5;4m"
    purple = "\033[38;5;20m"

    # Allowed characters
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"

    def __init__(self, user):
        self.data = user

    # Brute force function
    def tryPassword(self):

        start = time.time()
        attempts = 0
        for i in range(1, 9):
            for letter in itertools.product(self.chars, repeat=i):
                attempts += 1
                letter = ''.join(letter)

                if letter.rstrip() == self.data.rstrip():
                    distance = time.time() - start
                    print(self.pink+"Cracked the password in %s seconds and %s attempts!" % (distance, attempts))
                    print(self.green + "Password: ",end = '')
                    print(self.white + self.data,end='')
                    return
                
