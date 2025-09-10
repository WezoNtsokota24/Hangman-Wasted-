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
    print("####################")
    
    for line in hangman_steps[tries]:
        print(line)
    print("####################")

def display_hint(hint):
    print

def display_answer(answer):
    pass


def main():
    answer= random.choice(words)
    hint = ["_"]*len(answer)
    tries = 6
    guessed_letters = set()
    is_runnning = True
    
    while is_runnning:
        print("\n")
        display_hangman(tries)
        display_hint(hint)
        display_answer(answer)
        guess = input("Simon says Guess a letter: ").lower()
    
    

if __name__ == "__main__":
    main()







 


