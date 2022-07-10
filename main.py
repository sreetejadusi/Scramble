from itertools import permutations
from PyDictionary import *
class Begin:
    def __init__(self):
        print("Welcome To Scramble!")
        self.userinput = input("enter letters without spaces or commas: ").lower()

class ListGen:
    def __init__(self):

        self.wordlist = permutations(begin.userinput)
        self.finallist = []
        for x in list(self.wordlist):
            self.finallist.append(''.join(x))

class Compare:
    def __init__(self):
        for x in listgen.finallist:
            if PyDictionary.meaning(x) == None:
                pass
            else:
                print(x, ":", PyDictionary.meaning(x))

print("We Are Done!")


begin = Begin()
listgen = ListGen()
compare = Compare()