# Import all methods from the method file -- Also runs the file
#///from methods import *
import sys, getopt
from Methods.md5 import MD5

mode = []
inputPassword = 'password' + '\n'

def main(argv):
   # Initilize variables for use in running the proper method for encrypting or decrypting the password
   type = ''
   password = ''
   hash = ''

   # Takes in arguments from the command line
   try:
      opts, args = getopt.getopt(argv,"himd:o:")
   except getopt.GetoptError:
      #print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h"):
         print('Syntax:')
         mode.append(opt)
      elif opt in ("-i"):
         inputfile = arg
         mode.append(opt)
      elif opt in ("-o"):
         outputfile = arg
         mode.append(opt)
      elif opt in ("-d"):
         mode.append(opt)
      elif opt in ("-m"):
         mode.append(opt)
   decrypt(hash)


def decrypt(hash):
   print(mode)
   if '-i' in mode:
      print("*");
   if '-d' in mode:
      InputFile = open(r"passlist.txt","r")
      content = InputFile.readlines()
      #print(content)
      if inputPassword in content:
         print("password found!")
      InputFile.close()
   if '-m' in mode:
      print("lol")
      MD5.__init__('5a8dd3ad0756a93ded72b823b19dd877')
      print(MD5.decrypt('5a8dd3ad0756a93ded72b823b19dd877'))

if __name__ == "__main__":
   main(sys.argv[1:])
