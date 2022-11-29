# Import all methods from the method file -- Also runs the file
#///from methods import *
import sys, getopt, hashlib
from Methods.md5 import MD5

mode = []
inputPassword = str(input("Input password to be cracked:"))

def main(argv):
   # Initilize variables for use in running the proper method for encrypting or decrypting the password
   hash = ''

   # Takes in arguments from the command line
   try:
      opts, args = getopt.getopt(argv,"hmds:")
   except getopt.GetoptError:
      #print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h"):
         print('Syntax:')
         mode.append(opt)
      elif opt in ("-d"):
         mode.append(opt)
      elif opt in ("-m"):
         mode.append(opt)
      elif opt in ("-s"):
         mode.append(opt)
   decrypt(hash)


def decrypt(hash):
   print(mode)
   if '-d' in mode:
      InputFile = open(r"passList.txt","r")
      content = InputFile.readlines()
      #print(content)
      if inputPassword in content:
         print("password found!")
      InputFile.close()

   if '-m' in mode:
      print("lol")
      MD5.__init__('5a8dd3ad0756a93ded72b823b19dd877')
      print(MD5.decrypt('5a8dd3ad0756a93ded72b823b19dd877'))

   if '-s' in mode:
      hashedInput = hashlib.sha256(inputPassword.encode('utf-8'))
      #print ("what" + str(hashedInput))
      print(inputPassword)
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
if __name__ == "__main__":
   main(sys.argv[1:])
