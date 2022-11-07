'''
Author :- Vanshita Rohela
Description :- Number Guessing Game
Date :- 01.11.2022  4:40 PM
Udemy 100 Days of Python Bootcamp Angela Yu
'''

from random import randint
import os


def number_guess(guess):
    user_number = int(input("Make a guess: "))
    if user_number > guess:
        print("Too High.")
    elif user_number < guess:
        print("Too Low.")
    else:
        print("You guessed correctly.")
        return True


def play_game():
    print("Welcome to the")
    print("""
     _   _                 _                  _____                     _                                          
    | \ | |               | |                / ____|                   (_)                                         
    |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___ 
    | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ |
    | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
    |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                                                                __/ |   __/ |                     
                                                                                |___/   |___/                      

    """)
    print("I am thinking of a number between 1 and 100.")

    guess = randint(1, 100)


    user_choice = input("Choose a difficulty. Type 'easy' for 10 attempts and 'hard' for 5 attempts. ").lower()

    if user_choice == 'easy':
        for i in range(10, 0, -1):
            print(f"You have {i} attempts left to guess the number.")
            user_guess = number_guess(guess)
            if user_guess == True:
                break
            print("You have run out of guesses.")
            
        
    elif user_choice == 'hard':
        for i in range(5, 0, -1):
            print(f"You have {i} attempts left to guess the number.")
            user_guess = number_guess(guess)
            if user_guess == True:
                break
            print("You have run out of guesses.")

       
while input("To play the Number Guessing Game, type 'y', else 'n':  ").lower() == 'y':
    os.system('cls')
    play_game()
