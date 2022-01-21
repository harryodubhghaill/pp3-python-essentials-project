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

        self.title = f"\n{self.name}'s board"
        self.board = [["~"] * self.size for x in range(self.size)]

    def print_board(self):
        print(self.title)
        print("\n  " + " ".join(str(x) for x in range(1, self.size + 1)))
        for r in range(self.size):
            print(str(r + 1) + " " + " ".join(str(c) for c in self.board[r]))

    def place_ship(self):
        print(self)


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
    print("\nChoose your difficulty!\n\nEnter 'e' for Easy, 'm' for Medium, 'h' for Hard\n")

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


def game_init(difficulty, name):
    if difficulty == "e":
        player_board = Board(5, name, 4)
        return player_board
    elif difficulty == "m":
        player_board = Board(7, name, 6)
        return player_board
    elif difficulty == "h":
        player_board = Board(9, name, 8)
        return player_board
    else:
        print("Error")


def game_loop():
    clear_term()
    print_start()
    print_rules()
    player_name = get_name()
    print(f"\nWelcome to the game {player_name}")
    player_difficulty = choose_difficulty()
    player_board = game_init(player_difficulty, player_name)
    computer_board = game_init(player_difficulty, "Computer")
    player_board.print_board()
    computer_board.print_board()


game_loop()
