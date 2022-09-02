import random

from HangmanArt import states, logo
from HangmanWordList import word_list

print(logo)


# Choose a word by random module from a list filled with words
chosen_word: str = random.choice(word_list)

# to test the code
print(f"The chosen word is {chosen_word}")

string_list = ['_' for i in chosen_word]
lives = 6
guess_list = []

while lives > 0:
    # guess a letter
    guess = input("Enter a letter that you guess is in the word: ").lower()

    # if they have already guessed it, let them know
    if guess in guess_list:
        print("You have already made this guess. Don't Worry, it won't affect your number of lives.")
    else:
        # if letter wasn't in guess list then append it in the list
        guess_list.append(guess)
        # only if the guess letter is there, start the loop of replacing _ with the actual letter
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    string_list[i] = guess

        # If the letter isn't there first print the ascii art of the hangman and then reduce a life
        else:
            print(states[lives - 1])
            lives -= 1
    
    # print the list after every loop in the while loop
    # print(string_list)

    # better way to print the blanks and letters
    print(' '.join(string_list))

    # if before consuming all the lives the user guesses all letters correctly, break the loop with printing You Win!
    if '_' not in string_list:
        print("You Win!")
        break

# if after all the loops they still haven't guessed correctly, print You Lose!
if '_' in string_list:
    print("You Lose!")
