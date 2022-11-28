
class DictionaryAttack:

    def __int__(self):
        print('Running Dictionary Attack')
    def check(self, password):
        input_file = open(r"passlist.txt", "r")
        content = input_file.readlines()
        # print(content)
        if password in content:
            print("Password found!")
        else:
            print("That password is not in the top 10000 passwords.")
        input_file.close()
    def list(self, index):
        input_file = open(r"passlist.txt", "r")
        content = input_file.readlines()
        return content[index].strip()
        input_file.close()
