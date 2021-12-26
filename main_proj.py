import time


def welcome():
    name = input("Hello player! please enter your name: ")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(
        f"Hello {name}! and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    time.sleep(1)


welcome()


def load_game():
    print("Please choose a game to play: ")
    time.sleep(1)
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    time.sleep(1)
    print("2. Guess Game - guess a number and see if you chose like the computer")
    time.sleep(1)
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    try:
        chosen_game = input("What is your choice?(1 - 3) --> ")
        while not chosen_game.isdigit():
            chosen_game = input("You entered invalid number, choose again\n")

        while True:
            if chosen_game == "1":
                print("You chose a Memory Game! ")
                return 1
            elif chosen_game == "2":
                print("You chose a Guess Game! ")
                return 2
            elif chosen_game == "3":
                print("You chose a Currency Roulette! ")
                return 3
            else:
                chosen_game = input("You entered invalid number, choose again\n")
    finally:
        level_of_difficulty = input("Please choose game difficulty from 1 to 5: ")
        while not level_of_difficulty.isdigit():
            level_of_difficulty = input("You entered invalid number, choose again\n")

        while True:
            if level_of_difficulty == "1":
                print("You chose 1, Very easy! ")
                return 101
            elif level_of_difficulty == "2":
                print("You chose 2, Easy! ")
                return 102
            elif level_of_difficulty == "3":
                print("You chose 3, Normal! ")
                return 103
            elif level_of_difficulty == "4":
                print("You chose 4, Hard! ")
                return 104
            elif level_of_difficulty == "5":
                print("You chose 5, Impossible! ")
                return 105
            else:
                level_of_difficulty = input("You entered invalid number, choose again\n")


load_game()
