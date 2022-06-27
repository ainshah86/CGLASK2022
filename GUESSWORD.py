import random


words = ["HYDOGEN","LITHIUM","SODIUM","CALCIUM","POTASSIUM","TITANIUM"]

word=random.choice(words)
print("GUESS THE ELEMENT")
guesses=''

turns=3
    
while turns>0:
            failed=0

            for char in word:

                if char in guesses:
                    print(char, end=" ")
                
                else:
                    print("_")
                    print(char,end=" ")

                    failed+=1
            if failed==0:
                print("you win")

                print("the word is:",word)
                break
            print()
            guess=input("guess a character:")

            guesses+=guess
            if guess not in word:

                turns-=1

                print("wrong")

                print("you have",+turns,'more guesses')

                if turns==0:
                    print("you loose")




