import sys
import random
from enum import Enum


def guess(name="PlayerOne"):
    winning_percentage = 0
    game_count = 0
    player_wins = 0

    def guess_number():
        nonlocal name
        nonlocal player_wins

        class GUESSES(Enum):
            ONE = 1
            TWO = 2
            THREE = 3

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return guess_number()

        player_selection = int(playerchoice)

        computerchoice = random.choice("123")

        computer_selection = int(computerchoice)

        print(
            f"\n{name}, you chose {str(GUESSES(player_selection)).replace('GUESSES.', '').title()}."
        )
        print(
            f"I was thinking of {str(GUESSES(computer_selection)).replace('GUESSES.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😢"

        game_result = decide_winner(player_selection, computer_selection)

        print(game_result)

        nonlocal game_count
        game_count += 1
        nonlocal winning_percentage
        winning_percentage = player_wins / game_count * 100

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {winning_percentage:.2f}%")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    guessing_game = guess(args.name)
    guessing_game()
