
class DictionaryAttack:
    
    # Defines dictionary as a big variable
    content = ""
    
    # Color Codes!
    white = "\033[38;5;252m"
    pink = "\033[38;5;5m"
    red = "\033[38;5;1m"
    orange = "\033[38;5;3m"
    green = "\033[38;5;150m"
    blue = "\033[38;5;4m"
    purple = "\033[38;5;20m"
    
    # Initialize the function
    def __init__(self):
        print(self.blue+"Running Dictionary Attack")
    
    # Return the size of the dictionary file
    def dictSize(self):
        # Open the dictionary file and store it in content
        with open(r"bigDict.txt", 'r') as pg:
            self.content = pg.readlines()
            dictSize = len(self.content)
        # Returns the length of content
        return dictSize
    
    # Check to see if a password is in the dictionary
    def check(self, password):
        # Adds a new line seperator to the end of the password (because why truncate the whole dictionary 😔)
        password += "\n"
        # Defines the size of the dictionary to report in the print statement
        size = DictionaryAttack.dictSize(self)
        # If the password is found in the dictionary, print the fun stuff 😄, otherwise print the sad stuff 🥲
        if password in self.content:
            print(self.green+"Password found in the top " + str(size) + " most common passwords!")
            print("Password: "+ self.white + password, end='')
        else:
<<<<<<< HEAD
            print(self.red+"That password is not in the top " + str(size) + " passwords.")

=======
            print("That password is not in the top " + str(size) + " passwords.")
    
    # For use in other methods, return plaintext for the password at the intex requested
>>>>>>> 52132a8403059afad60e9e29e0db111505edab79
    def list(self, index):
        return self.content[index].strip()
