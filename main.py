# Import all methods from the method file -- Also runs the file
# ///from methods import *
import sys, getopt
from Methods.md5 import MD5
from Methods.dictionaryAttack import DictionaryAttack

mode = []
# Moved to flag if-statements to allow for prompts to be customizable for each hash
inputPassword = str(input("Input password to be cracked:")) + '\n'


def main(argv):
    # Initialize variables for use in running the proper method for encrypting or decrypting the password

    # Takes in arguments from the command line
    try:
        opts, args = getopt.getopt(argv, "hmd:")
    except getopt.GetoptError:
        # print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in "-h":
            print('Syntax:')
            mode.append(opt)
        elif opt in "-d":
            mode.append(opt)
            user = str(input("Input hash to be cracked: ")) + "\n"
            decrypt(user)
        elif opt in "-m":
            mode.append(opt)
            #eod = input("1 for encrypt, 2 for decrypt")
            #if eod == 1:
            #    encrypt(str(input("Input hash to be cracked: ")))
            #if eod == 2:
            #    decrypt(str(input("Input hash to be cracked: ")))


# Methods for decrypting a file
def decrypt(variable):
    if '-d' in mode:
        runner = DictionaryAttack()
        print(runner.check(variable))
    if '-m' in mode:
        print("Cracking..... \n")
        runner = MD5(variable)
        print(runner.decrypt())


# This is mostly just a convenience.
def encrypt(variable):
    if '-m' in mode:
        runner = MD5(variable)
        print(runner.encrypt())
