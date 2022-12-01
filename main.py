# Import all methods from the method file -- Also runs the file
# ///from methods import *
import sys, getopt
from Methods.md5 import MD5
from Methods.sha256 import SHA256
from Methods.dictionaryAttack import DictionaryAttack
from Methods.bcrypt import BCrypt
from Methods.bruteForce import BruteForce

mode = []

white = "\033[38;5;252m"
pink = "\033[38;5;5m"
red = "\033[38;5;1m"
orange = "\033[38;5;3m"
green = "\033[38;5;150m"
blue = "\033[38;5;4m"
purple = "\033[38;5;20m"


def main(argv):
    # Initialize variables for use in running the proper method for encrypting or decrypting the password

    # Takes in arguments from the command line
    try:
        opts, args = getopt.getopt(argv, "hmsdfbx:")
    except getopt.GetoptError:

        sys.exit(2)
    for opt, arg in opts:

        eod = 0
        if (opt in "-m") or (opt in "-s") or (opt in "-b"):
            eod = int(input(pink + "1 for Encrypt, 2 for Decrypt: "))

        if opt in ("-h"):
            print(blue + "Syntax: ")
            mode.append(opt)
        elif opt in "-d":
            mode.append(opt)
            decrypt(str(input(red + "Input password to be cracked: " + white)) + "\n")
        elif opt in "-f":
            mode.append(opt)
            decrypt(str(input(red + "Input password to be cracked through brute force: " + white)) + "\n")
        elif opt in ("-m"):
            mode.append(opt)
        elif opt in '-s':
            mode.append(opt)
        elif opt in '-b':
            mode.append(opt)

        if eod == 1:
                encrypt(str(input(blue + "Password to be hashed: " + white)))
        elif eod == 2:
                decrypt(str(input(red + "Input hash to be cracked: " + white)))


# Methods for decrypting a file
def decrypt(variable):
    print(red + "Cracking..... ")
    if '-d' in mode:
        runner = DictionaryAttack()
        runner.check(variable)
    if '-f' in mode:
        runner = BruteForce(variable)
        runner.fPrint()
    if '-m' in mode:
        runner = MD5(variable)
        runner.decrypt()
    if '-s' in mode:
        runner = SHA256(variable)
        runner.dictDecrypt()
    if '-b' in mode:
        runner = BCrypt(variable)
        runner.decrypt()


# This is mostly just a convenience.
def encrypt(variable):
    print(blue + "Encrypting..... ")
    if '-m' in mode:
        runner = MD5(variable)
        print(green + "Password: " + white + str(variable))
        print(green + "MD5 Encrypted: " + white + runner.encrypt())
    if '-s' in mode:
        runner = SHA256(variable)
        print(green + "Password: " + white + str(variable))
        print(green + "SHA256 Encrypted: " + white + runner.encrypt())
    if 'b' in mode:
        runner = BCrypt(variable)
        print(green + "Password: " + white + str(variable))
        print(green + "BCrypt Encrypted: " + white + runner.encrypt())

if __name__ == "__main__":
    main(sys.argv[1:])
