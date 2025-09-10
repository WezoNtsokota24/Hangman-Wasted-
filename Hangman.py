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
#for line in hangman_steps[6]:
#    print(line)

def display_hangman(tries):
    print("####################")
    
    for line in hangman_steps[tries]:
        print(line)
    print("####################")

def display_hint(hint):
    print(" ".join(hint))
    

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer= random.choice(words)
    hint = ["_"]*len(answer)
    tries = 0

    
    guessed_letters = set()
    is_runnning = True
    
    while is_runnning:
        print("\n")
        display_hangman(tries)
        display_hint(hint)
        guess = input("Simon says Guess a letter: ").lower()
        
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
            
        if guess in guessed_letters:
            print(f"{guess} already guessed. Try again.")
            continue
        
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    
        
        else: 
            tries += 1
            
        if "_" not in hint:
            display_hangman(tries)
            display_answer(answer)
            print("Congratulations! You've guessed the word correctly!")
            is_runnning = False
        elif tries >= len(hangman_steps)-1:
            display_hangman(tries)
            print(f"Sorry, you've run out of tries. The word was '{answer}'.")
            is_runnning = False
            
            
    
    
    

if __name__ == "__main__":
    main()
