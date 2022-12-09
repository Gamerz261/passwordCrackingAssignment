# Import all methods from the method file -- Also runs the file
import sys, getopt
from Methods.md5 import MD5
from Methods.sha256 import SHA256
from Methods.dictionaryAttack import DictionaryAttack
from Methods.bcrypt import BCrypt
from Methods.bruteForce import BruteForce

white = "\033[38;5;250m"
pink = "\033[38;5;5m"
red = "\033[38;5;1m"
orange = "\033[38;5;3m"
green = "\033[38;5;150m"
blue = "\033[38;5;74m"
purple = "\033[38;5;210m"
clay = "\033[38;5;95m"
blue1 = "\033[38;5;218m"
blue2 = "\033[38;5;217m"
blue3 = "\033[38;5;216m"
blue4 = "\033[38;5;215m"


def main(argv):
    #print(sys.argv)
    userIn = str(sys.argv[len(sys.argv)-1]).encode('utf-8') # Takes in arguments from the command line

    if len(sys.argv)<2: # If no arguments are given, print a helpful tip.
        print("No arguments given. Use -h for more info.")

    try:
        opts, args = getopt.getopt(argv, "hmsbcfydex:") # All flag options
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if '-h' in sys.argv:
            print(clay + "Syntax: $~python3 main.py <Flags> <Hash or Plain-Text>\n")
            print(purple + "\u2690 Flags: ")
            print(blue1+" '-h' - Help")
            print(blue2+" \u2937 Hashing Algorithms:\n  '-m' - md5\n  '-s' - SHA256\n  '-b' - BCrypt")
            print(blue3+" \u2937 Must be used alongside a hashing algorithm:\n  '-e' - Encrypt\n  '-d' - Decrypt")
            print(blue4+" \u2937 Can be used alongside a hashing algorithm or standalone:\n  '-d' - Dictionary Attack\n  '-f' - Brute Force")
        elif '-e' in sys.argv: # Else, run the encrypt method
            encrypt(str(userIn))
            break
        elif opt in '-b':
            decrypt(str(input(red + "Input hash to be cracked: " + white)))
            break
        elif opt in ['-d','-f','-c']: # The decrpyt method will run for dictionary and brute force with this too.
            decrypt(str(userIn))
            break
        

# Methods for decrypting a file
def decrypt(variable):
    if '-c' in sys.argv:
        runner = DictionaryAttack()
        runner.check(variable)
        return
    print(red + "Cracking..... ")
    if '-f' in sys.argv:
        runner = BruteForce(variable)
        runner.fPrint()
    elif '-m' in sys.argv:
        runner = MD5(variable)
        runner.decrypt()
    elif '-s' in sys.argv:
        runner = SHA256(variable)
        runner.dictDecrypt()
    elif '-b' in sys.argv:
        runner = BCrypt(variable)
        runner.decrypt()
    else:
        print(red+"No hashing algorithm given to decrypt. See -h for more info.")

def encrypt(variable):
    print(blue + "Encrypting..... ")
    if '-m' in sys.argv:
        runner = MD5(variable)
        print(green + "Password: " + white + str(variable))
        print(green + "MD5 Encrypted: " + white + runner.encrypt())
    elif '-s' in sys.argv:
        runner = SHA256(variable)
        print(green + "Password: " + white + str(variable))
        print(green + "SHA256 Encrypted: " + white + runner.encrypt())
    elif '-b' in sys.argv:
        runner = BCrypt(variable)
        print(green + "Password: " + white + str(variable)[2:-1])
        print(green + "BCrypt Encrypted: " + white + str(runner.encrypt())[2:-1])
    else:
        print(red+"No hashing algorithm given to encrypt. See -h for more info.")

if __name__ == "__main__":
    main(sys.argv[1:])
