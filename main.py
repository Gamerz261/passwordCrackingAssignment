# Import all methods from the method file -- Also runs the file
#///from methods import *
import sys, getopt
from Methods.md5 import MD5
from Methods.sha256 import SHA256
from Methods.dictionaryAttack import DictionaryAttack

mode = []

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
         eod = int(input("1 for Encrypt, 2 for Decrypt: "))

      if opt in ("-h"):
         print('Syntax:')
         mode.append(opt)
      elif opt in "-d":
         mode.append(opt)
         decrypt(str(input("Input hash to be cracked: ")) + "\n")
      elif opt in ("-m"):
         mode.append(opt)
         if eod == 1:
            encrypt(str(input("Password to be hashed: ")))
         if eod == 2:
            decrypt(str(input("Input hash to be cracked: ")))
      elif opt in '-s':
         mode.append(opt)
         if eod == 1:
            encrypt(str(input("Password to be hashed: ")))
         if eod == 2:
            decrypt(str(input("Input hash to be cracked: ")))


# Methods for decrypting a file
def decrypt(variable):
    if '-d' in mode:
        runner = DictionaryAttack()
        print(runner.check(variable))
    if '-m' in mode:
        print("Cracking..... \n")
        runner = MD5(variable)
        print(runner.decrypt())
    if '-s' in mode:
        print("Cracking..... \n")
        runner = SHA256()
        print(decrypt(runner))


# This is mostly just a convenience.
def encrypt(variable):
    if '-m' in mode:
        print("Encrypting..... \n")
        runner = MD5(variable)
        print(runner.encrypt())
    if '-s' in mode:
        print("Encrypting..... \n")
        runner = SHA256(variable)
        print(runner.encrypt())

if __name__ == "__main__":
    main(sys.argv[1:])