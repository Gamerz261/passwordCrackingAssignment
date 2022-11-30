# Import all methods from the method file -- Also runs the file
#///from methods import *
import sys, getopt, bcrypt
from Methods.md5 import MD5
from Methods.sha256 import SHA256
from Methods.dictionaryAttack import DictionaryAttack

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
      opts, args = getopt.getopt(argv,"hmsd:")
   except getopt.GetoptError:
      #print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:

      if ((opt in ("-m")) or (opt in ("-s"))):
         eod = int(input(purple + "1 for Encrypt, 2 for Decrypt: "))

      if opt in ("-h"):
         print(blue + "Syntax: ")
         mode.append(opt)
      elif opt in "-d":
         mode.append(opt)
         decrypt(str(input(red + "Input hash to be cracked: ")) + "\n")
      elif opt in ("-m"):
         mode.append(opt)
         if eod == 1:
            encrypt(str(input(blue + "Password to be hashed: ")))
         if eod == 2:
            decrypt(str(input(red + "Input hash to be cracked: ")))
      elif opt in '-s':
         mode.append(opt)
         if eod == 1:
            encrypt(str(input(blue + "Password to be hashed: ")))
         if eod == 2:
            decrypt(str(input(red + "Input hash to be cracked: ")))

# Methods for decrypting a file
def decrypt(variable):
    if '-d' in mode:
        runner = DictionaryAttack()
        print(runner.check(variable))
    if '-m' in mode:
        print("Cracking..... ")
        runner = MD5(variable)
        print(runner.decrypt())
    if '-s' in mode:
        print("Cracking..... ")
        print(SHA256.decrypt(0, variable))


# This is mostly just a convenience.
def encrypt(variable):
    if '-m' in mode:
        print("Encrypting..... ")
        runner = MD5(variable)
        print(runner.encrypt())
    if '-s' in mode:
        print("Encrypting..... ")
        print(green + "SHA256 Encrypted:", end = ' ')
        print(white + SHA256.encrypt(0, variable))

if __name__ == "__main__":
    main(sys.argv[1:])