from art import logo, vs
from gamedata import data
from random import choice
import os


def represent_data(dictionary):
    """Represents the name, description and country of the account."""
    first_user_name = dictionary['name']
    first_user_description = first_user_dict["description"]
    first_user_country = first_user_dict["country"]
    return f"{first_user_name}, {first_user_description}, from {first_user_country}."


def compare(input, first_dict, second_dict):
    """Returns True if according to user input guess in correct, else False."""
    first_followers = first_dict['follower_count']
    second_followers = second_dict['follower_count']
    if input == 'a':
        return first_followers > second_followers
    elif input == 'b':
        return second_followers > first_followers


print(logo)
second_user_dict = choice(data)
score = 0


while True:
    # assign values A and B
    first_user_dict = second_user_dict 
    second_user_dict = choice(data)
    while second_user_dict == first_user_dict:
        second_user_dict = choice(data)

    
    # representing the values of A and B
    print(f"Compare A: {represent_data(first_user_dict)}")
    print(vs)
    print(f"Againts B: {represent_data(second_user_dict)}")

    # Taking user input
    user_input = input("Who has more followers? Type 'A' or 'B'. ").lower()

    os.system('cls')
    print(logo)


    # Calling compare function defined above
    if compare(user_input, first_user_dict, second_user_dict) == True:
        score += 1
        print(f"You're right! Current Score: {score}")
        
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        break
