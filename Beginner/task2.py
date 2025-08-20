'''
Practical Test: Develop a number guessing game where the program selects a random
number, and the user tries to guess it within a limited number of attempts.
'''

import random

def random_number():
    return random.randint(1,99)

def main():

    no_of_guesses = 10
    guesses = 0
    
    computer_number = random_number()
    print(computer_number)

    while guesses < no_of_guesses:
        guessed_number = int(input("Guess the number: "))
        if guessed_number == computer_number:
            print("You guessed the number correctly!")
            guesses += 1
            break
        else:
            print("Try again")
            guesses += 1
            if guesses == no_of_guesses:
                print("You ran out of guesses!")

if __name__ == "__main__":
    main()