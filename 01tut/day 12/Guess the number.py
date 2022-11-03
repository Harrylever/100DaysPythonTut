import random

print("Guess the number")
print("Welcome to the Number Guessing Game")

player_play_again = True


def run_n_g_g():
    global player_play_again
    print("I'm thinking of a number between 1 and 100.")
    game_number = random.randrange(1, 100)
    easy_level_attempts = 10
    hard_level_attempts = 5
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == "easy":
        while easy_level_attempts > 0 and player_play_again:
            print(f"You have {easy_level_attempts} attempts to guess the number.")
            player_guess = int(input("Make a guess: "))
            if player_guess > game_number:
                easy_level_attempts -= 1
                print("Too high.")
                if easy_level_attempts > 0:
                    print("Guess again.")
            elif player_guess < game_number:
                easy_level_attempts -= 1
                print("Too low.")
                if easy_level_attempts > 0:
                    print("Guess again.")
            elif player_guess == game_number:
                print(f"You got it! The answer was {game_number}.")
                play_again = input("Do you want to play again? 'Yes' or 'No': ").lower()
                if play_again == "no":
                    easy_level_attempts = 0
                    player_play_again = False
                else:
                    run_n_g_g()
        if easy_level_attempts == 0 and player_play_again:
            print("You've run out of guesses, you lose.")
            return
        elif easy_level_attempts == 0 and player_play_again is False:
            print("Goodbye...")
            return
    elif game_level == "hard":
        while hard_level_attempts > 0 and player_play_again:
            print(f"You have {hard_level_attempts} attempts to guess the number.")
            player_guess = int(input("Make a guess: "))
            if player_guess > game_number:
                hard_level_attempts -= 1
                print("Too high.")
                if hard_level_attempts > 0:
                    print("Guess again.")
            elif player_guess < game_number:
                hard_level_attempts -= 1
                print("Too low.")
                if hard_level_attempts > 0:
                    print("Guess again.")
            elif player_guess == game_number:
                print(f"You got it! The answer was {game_number}.")
                play_again = input("Do you want to play again? 'Yes' or 'No': ").lower()
                if play_again == "no":
                    hard_level_attempts = 0
                    player_play_again = False
                else:
                    run_n_g_g()
        if hard_level_attempts == 0 and player_play_again:
            print("You've run out of guesses, you lose.")
            print(f"The game number was {game_number}")
            return
        elif hard_level_attempts == 0 and player_play_again is False:
            print("Goodbye...")
            return
    while player_play_again:
        run_n_g_g()


run_n_g_g()
