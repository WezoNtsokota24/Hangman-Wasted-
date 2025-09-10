#Hangman with no hangover :)
#from wordslist import words 
import random

words = ('burger', 'pizza', 'gatsby', 'nachos', 'taco')
 
#dictionary of key :()

hangman_steps = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "), 
                2: (" o ",
                    " |  ",
                    "   "),
                3: (" o ",
                    "/|  ",
                    "   "),
                4: (" o ",
                    "/|\\  ",
                    "   "),
                5: (" o ",
                    "/|\\ ",
                    "/  "),
                6: (" o ",
                    "/|\\  ",
                    "/ \\  "),}

#print(hangman_steps[0])

def display_hangman(tries):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass


def main():
    pass

if __name__ == "__main__":
    main()







 


