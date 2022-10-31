from random import choice
import os



def compare_cards(user, comp, user_list, comp_list):
    if user > 21:
        return "You went over 21. You lost!"
    elif comp > 21:
        return "Computer went over 21. You win!"
    elif comp == 21 and len(comp_list) == 2:
        return "Computer hit a BlackJack. You lose!"
    elif user == 21 and len(user_list) == 2:
        return "You hit a BlackJack. You win!"
    elif user == comp:
        return "It's a draw."
    elif user > comp:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """Use this function to play the game as long as the user wants."""

    print("""
    Welcome to the game of

    .------..------..------..------..------..------..------..------..------.
    |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
    | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
    | ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
    | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
    `------'`------'`------'`------'`------'`------'`------'`------'`------'
    """)

    # write list of possible card numbers
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    computer_cards = []
    user_cards = []

    # adding two cards to both the lists
    for _ in range(2):
        computer_cards.append(choice(cards))
        user_cards.append(choice(cards))

    # printing user cards and computer's first card.
    print(f"Your cards are {user_cards} and your score is {sum(user_cards)}.")
    print(f"Computer's first card is {computer_cards[0]}.\n")

    # adding cards to user list
    while input("Type 'y' to add a card else type 'n'. ").lower() == 'y':
        random_number = choice(cards)
        if random_number == 11 and (sum(user_cards) + 11) > 21:
            user_cards.append(1)
        else:
            user_cards.append(random_number)

        print(
            f"You cards are {user_cards} and your score is {sum(user_cards)}.\n")

    # adding cards to the computer list
    while sum(computer_cards) < 17:
        random_number = choice(cards)
        if random_number == 11 and (sum(computer_cards) + 11) > 21:
            computer_cards.append(1)
        else:
            computer_cards.append(random_number)

    user_score = sum(user_cards)
    comp_score = sum(computer_cards)

    # printing scores and finally who won
    print(
        f"Your score is {user_score} and computer's score is {comp_score}.\n")
    print(compare_cards(user_score, comp_score, user_cards, computer_cards))
    print()


while input("If you want to play BlackJack, enter 'y' else 'n'. ").lower() == 'y':
    # clearing the screen so when it loops, previous game gets cleared
    os.system('cls')
    play_game()
