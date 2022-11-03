import random
import sys
from art import logo


number_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def run_blackjack():
    """Run BlackJack Function 🙃"""
    player_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if player_play == "n":
        print("Come back later. Goodbye...")
        sys.exit()
    else:
        blackjack()


def blackjack():
    print(logo)
    player_cards = []
    computer_cards = []
    for i in range(2):
        random_number_player = random.choice(number_list)
        random_number_computer = random.choice(number_list)
        while random_number_player in player_cards:
            random_number_player = random.choice(number_list)
        player_cards.append(random_number_player)
        while random_number_computer in computer_cards:
            random_number_computer = random.choice(number_list)
        computer_cards.append(random_number_computer)

    print()
    print("Blackjack")
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if get_another_card == "y":
        should_get_another_card = True
        while should_get_another_card:
            random_number_player = random.choice(number_list)
            player_cards.append(random_number_player)
            computer_get_another_card_values = [0, 1]
            computer_get_another_card = random.choice(computer_get_another_card_values)
            if computer_get_another_card == 1:
                random_number_computer = random.choice(number_list)
                computer_cards.append(random_number_computer)
            print(f"Your cards: {player_cards}")
            print(f"Computer's first card: {computer_cards[0]}")

            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == "n":
                print(f"Your final hand: {player_cards}")
                print(f"Computer's final hand: {computer_cards}")
                player_cards_final_value = 0
                computer_cards_final_value = 0
                for player_cards_value in player_cards:
                    player_cards_final_value += player_cards_value
                for computer_cards_value in computer_cards:
                    computer_cards_final_value += computer_cards_value
                if player_cards_final_value < 21:
                    if player_cards_final_value > computer_cards_final_value:
                        print("You win")
                    elif player_cards_final_value == computer_cards_final_value:
                        print("Draw")
                    else:
                        print("You lose. Computer has higher card count")
                else:
                    print("You lose card is higher than 21.")
                should_get_another_card = False
    else:
        print(f"Your final hand: {player_cards}")
        print(f"Computer's final hand: {computer_cards}")
        player_cards_final_value = 0
        computer_cards_final_value = 0
        for player_cards_value in player_cards:
            player_cards_final_value += player_cards_value
        for computer_cards_value in computer_cards:
            computer_cards_final_value += computer_cards_value
        if player_cards_final_value < 21:
            if player_cards_final_value > computer_cards_final_value:
                print("You win")
            elif player_cards_final_value == computer_cards_final_value:
                print("Draw")
            else:
                print("You lose. Computer has higher card count")
        else:
            print("You lose card is higher than 21.")
        should_get_another_card = False
    run_blackjack()


run_blackjack()

# hello
