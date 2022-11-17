# Import all methods from the method file -- Also runs the file
#///from methods import *
import sys, getopt


mode = []

def main(argv):
   # Initilize variables for use in running the proper method for encrypting or decrypting the password
   type = ''
   password = ''
   hash = ''

   # Takes in arguments from the command line
   try:
      opts, args = getopt.getopt(argv,"hi:o:")
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
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
   decrypt()
   

def decrypt():
   if '-i' in mode:
      print("*");

if __name__ == "__main__":
   main(sys.argv[1:])