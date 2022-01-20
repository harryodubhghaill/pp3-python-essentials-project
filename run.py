import os


class Ship():
    """
    Defines Ship class with properties for placement and methods
    to track position and status
    """
    def __init__(self, size, orientation, start_coord, boat_type):
        self.size = size

        if orientation == 'h' or orientation == 'v':  # value check
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'h' or 'v'.")

        self.start = start_coord

        self.boat_type = boat_type

    def get_coords(self, size):
        print(size)


class Board():
    """
    Defines Board class that takes parameters for size and number of
    ships depending on difficulty. Takes name parameter to differentiate
    comp vs player board.
    """
    def __init__(self, size, name, num_ships):
        self.size = size
        self.name = name
        self.num_ships = num_ships

        self.board = [["~" for x in range(size)] for y in range(size)]

    def print_board(self, board):
        print(board)

    def place_ship(self):
        print(self)


# player_board = Board(9, player, 5)

# player_board.print_board()

# utility function to clear terminal
def clear_term():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # check for os
        command = 'cls'
    os.system(command)


def print_start():
    start_screen = ("~"*50)+"\n"+("~"*50) + "\n~~~~~~     WELCOME TO BATTLESHIP ROYAL      ~~~~~~\n"+ "~~  OBJECTIVE: TOTAL DESTRUCTION OF YOUR ENEMY  ~~\n" + ("~"*50)+"\n"+("~"*50)
    print(start_screen)


def print_rules():
    rules = "\n** HOW TO PLAY **\n" + "\nType our name into the field below\n" + "Select your Difficulty\n" + "Place your ships\n" + "Fire missiles at your opponents ships\n" + "Winner is first to clear all enemy ships\n"
    print(rules)


def get_name():
    player_name = input("Please enter your name: ")

    return player_name


def choose_difficulty():
    print("\nChoose your difficulty!\n Enter 'e' for Easy, 'm' for Medium, 'h' for Hard\n")

    while True:
        try:
            difficulty = input("Enter Difficulty Level: ")

            difficulty_options = ("e", "m", "h")
            if difficulty in difficulty_options:
                return difficulty
            else:
                print("Sorry, that's not an accepted value! Please try again")
        except ValueError:
            print("Please try again.")


def game_loop():
    clear_term()
    print_start()
    print_rules()
    print(f"\nWelcome to the game {get_name()}")
    print(choose_difficulty())


game_loop()
