import random
from game_data import data

logo = "Higher\nLower\n"
print(logo.upper())
vs_logo = "VS"


def choose_random_number():
    """Choose a random number"""
    # random.choice()
    random_number = random.randint(0, len(data) - 1)
    return random_number


def choose_first_game_data(random_number):
    """Return Information of Person to Show First on the Game."""
    first_val_data = data[random_number]
    return first_val_data


def choose_second_game_data(random_number):
    """Return Information of Person to Show Second on the Game."""
    second_val_data = data[random_number]
    return second_val_data


def comparing_val(first_val_data, second_val_data, ):
    """Compare the value of followers of the Two personalities."""
    compare1_stat = f"Compare A: {first_val_data['name']}, {first_val_data['description']}, from {first_val_data['country']}"
    compare2_stat = f"Against B: {second_val_data['name']}, {second_val_data['description']}, from {second_val_data['country']}"
    print(compare1_stat)
    print(vs_logo.upper())
    print(compare2_stat)
    compare_stat_val = input("Who has more followers? Type 'A' or 'B': ").upper()
    if compare_stat_val == "A":
        if first_val_data['follower_count'] > second_val_data['follower_count']:
            return True
        else:
            return False
    else:
        if second_val_data['follower_count'] > first_val_data['follower_count']:
            return True
        else:
            return False


def run_game():
    game_continue = True
    rand_number1 = choose_random_number()
    game_score = 0
    while game_continue:
        first_val = choose_first_game_data(random_number=rand_number1)
        rand_number2 = choose_random_number()
        while rand_number2 == rand_number1:
            rand_number2 = choose_random_number()
        second_val = choose_second_game_data(random_number=rand_number2)
        if data[rand_number1]['follower_count'] > data[rand_number2]['follower_count']:
            highest_val_owner = rand_number1
        else:
            highest_val_owner = rand_number2
        continue_val = comparing_val(first_val_data=first_val, second_val_data=second_val)
        if continue_val is False:
            game_continue = False
            print(f"Sorry, that's wrong! Final Score {game_score}")
        else:
            game_score += 1
            rand_number1 = highest_val_owner
            print(f"\n{logo.upper()}")
            print(f"You're right! Current Score {game_score}")
    print("\nGoodbye...")


run_game()
