import random

Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"

# rock and paper => paper
# if player choice greater than computer choice player win
# rock and scissors => rock
# paper and scissors => scissors
# 2 1 win   scissors and paper => scissors
# 1 0 win   paper and rock => paper
# 0 2 win   rock and scissors => rock
# 2 0 lose  scissors and rock => rock
# 1 1 draw  scissors and scissors => draw
# 1 0 win   rock and rock => draw
# 0 0 draw  paper and paper => draw
# 0 1 lose
# 0 2 lose

# Scissors = "Scissors"
# Paper = "Paper"
# Rock = "Rock"
#
# Scissors = "Scissors"
# Rock = "Rock"
# Paper = "Paper"
#
# Rock = "Rock"
# Paper = "Paper"
# Scissors = "Scissors"

RPS = [Rock, Paper, Scissors]

while True:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n: "))
    computer_choice = random.randint(0, 2)
    print(computer_choice)
    print("=*" * 30)

    if player_choice == 0 or player_choice == 1 or player_choice == 2:
        if player_choice == computer_choice:
            print(f"Computer chose {computer_choice}")
            print(RPS[computer_choice])
            print(f"You chose {player_choice}")
            print(RPS[player_choice])
            play_again = input("It's a Draw. Do you want to play again? 'Yes' or 'No'")
            if play_again == "Yes":
                continue
            elif play_again == "No":
                print("Okay. Goodbye")
                break
            else:
                print("Please enter a correct answer")
        elif (player_choice != 2 and computer_choice != 0) and player_choice > computer_choice:
            print(f"Computer chose {computer_choice}")
            print(RPS[computer_choice])
            print(f"You chose {player_choice}")
            print(RPS[player_choice])
            print("You win")
            play_again = input("Do you want to play again? 'Yes' or 'No'")
            if play_again == "Yes":
                print("Okay.")
            elif play_again == "No":
                print("Okay. Goodbye")
                break
            else:
                print("Please enter a correct answer")
        else:
            print(f"Computer chose {computer_choice}")
            print(RPS[computer_choice])
            print(f"You chose {player_choice}")
            print(RPS[player_choice])
            print("You lose")
    else:
        print("Bad Decision")
        # print(type(player_choice))
        print("Type 0 for Rock, 1 for Paper and 2 for Scissors")
