

import random

def main():

    words=["HYDOGEN","LITHIUM","SODIUM","CALCIUM","POTASSIUM","TITANIUM"]
    x=random.choice(words)
    print("GUESS THE ELEMENT")
    guesses=''

    turns=3
    
    while turns>0:
            failed=0

            for char in words:

                if char in guesses:
                    print(char, end=" ")
                
                else:
                    print("_")
                    print(char,end=" ")

                    failed+-1
            if failed==0:
                print("you win")

                print("the word is:",words)
                break
            print()
            guess=input("guess a character:")

            guesses+=guess
            if guess not in words:

                turns-=1

                print("wrong")

                print("you have",+turns,'more guesses')

                if turns==0:
                    print("you loose")

main()



