#This is a 'Guess The Word' game

import random

#Creating the words and their corresponding hints for the game
words = ['champion', 'guess', 'code', 'linux', 'screen']
hints = ["You become when you win", "You are playing", "What made this game?", "An OS", "You are looking at"]

while True:

    #Getting the welcome screen ready
    print()
    print()
    print("\t\t\t\t\t\t**** Welcome To 'Guess The Word' Game ****")
    print()

    #Creating the counter for user to input the letter and generating the word to guess
    chance = 4
    print(f"You have {chance} chance(s) left")
    b = random.randint(0,4)
    chosen_word = words[b]

    #Counting the length of the word and printing it
    l = len(chosen_word)
    print()
    print(f"Your word has {l} characters")
    print()

    #Creating the hint segment
    hi = input("Enter 'h' for hint and any other key to continue without hint: ")
    print()
    if hi.lower() == 'h':
        print(hints[b])
        print()

    #Taking the input, checking the answer and printing the response
    # '_' is used in 'for loop' to iterate certain number of times without a loop variable
    for _ in range (chance):
        user_input = input("Enter your answer: ")
        if user_input == chosen_word:
            print()
            print("Your answer is correct. Congratulations.")
            print()
            break
        else:
            chance -= 1
            print()
            print(f"Wrong answer. You have {chance} chance(s) left")
            print()
            if chance == 0:
                print(f"Your answer is wrong. The correct word was '{chosen_word}' ")
                print()
            
    #Segment to replay the game
    again = input("Enter 'p' to play again: ") 
    if again.lower() != 'p':
        print()
        print("Thanks for playing. Come Again.")
        print()
        break