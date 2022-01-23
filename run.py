import os


class Ship():
    """
    Defines Ship class with properties for placement and methods
    to track position and status
    """
    def __init__(self, size, orientation, start_coord):
        self.boat_size = size

        if orientation == 'h' or orientation == 'v':  # value check
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'h' or 'v'.")

        self.start = start_coord

    def get_coords(self):
        if self.orientation == 'h':
            if self.start[0] in range(0,6):
                self.coordinates = []
                for index in range(self.boat_size):
                    if self.start[1] + index in range(0,6):
                        self.coordinates.append({'row': self.start[0], 'col': self.start[1] + index})
                    else:
                        raise IndexError("Column is out of range.")
                return self.coordinates
            else:
                raise IndexError("Row is out of range.")
        elif self.orientation == 'v':
            if self.start[0] in range(0,6):
                self.coordinates = []
                for index in range(self.boat_size):
                    if self.start[1] + index in range(0,6):
                        self.coordinates.append({'row': self.start[0] + index, 'col': self.start[1]})
                    else:
                        raise IndexError("Row is out of range.")
                return self.coordinates
            else:
                raise IndexError("Column is out of range.")


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

        # creates styled line to print
        self.board = [["~"] * self.size for x in range(self.size)]
        self.logic_board = ([0] * self.size for x in range(self.size))

    def print_board(self):
        """
        Takes size and name from class to print styled and indexed play
        board.
        """
        print(self.title)
        print("\n  " + " ".join(str(x) for x in range(1, self.size + 1)))
        for r in range(self.size):
            print(str(r + 1) + " " + " ".join(str(c) for c in self.board[r]))

    def coords_guess(self, field):
        """
        Function to get guess from player. Field param is used to
        alternate use case.
        """
        while True:
            try:
                guess = int(input(f"{field} Guess: "))
                if guess in range(1, self.size + 1):
                    return guess - 1
                else:
                    print("\nOops, that's not even in the ocean.")
            except ValueError:
                print("\nPlease enter a number")

    def update_board(self, guess, symbol):
        """
        Takes guess and updates board to reflect.
        """
        self.board[guess['row']][guess['col']] = f'{symbol}'
        print(f"{self.name}'s board updated")

    def check_hit(self, ship_coords, guess_coords):
        if guess_coords in ship_coords:
            self.update_board(guess_coords, "X")
            print("Hit!")
        else:
            self.update_board(guess_coords, 'O')
            print("Miss!")

    # def update_ship(self, guess):
    #     """
    #     Takes guess and updates board to reflect.
    #     """
    #     self.logic_board[guess[0]][guess[1]] = 1
    #     print(f"{self.name}'s logic board updated")

    # def get_logic_board(self):
    #     board = list(map(int, self.logic_board))
    #     return board

    # def place_ship(self):
    #     print(self)


# utility function to clear terminal
def clear_term():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # check for os
        command = 'cls'
    os.system(command)


def print_start():
    start_screen = ("~"*50)+"\n"+("~"*50) + "\n~~~~~~     WELCOME TO BATTLESHIP ROYAL      ~~~~~~\n" + "~~  OBJECTIVE: TOTAL DESTRUCTION OF YOUR ENEMY  ~~\n" + ("~"*50)+"\n"+("~"*50)
    print(start_screen)


def print_rules():
    rules = "\n** HOW TO PLAY **\n" + "\nType your name into the field below\n" + "Select your Difficulty\n" + "Place your ships\n" + "Fire missiles at your opponents ships\n" + "Winner is first to clear all enemy ships\n"
    print(rules)


def get_name():
    player_name = input("Please enter your name: ")

    return player_name


def choose_difficulty():
    print("\nChoose your difficulty!\n")
    print("\nEnter 'e' for Easy, 'm' for Medium, 'h' for Hard\n")

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


def get_orientation():
    print("\nChoose Ship Orientation. Type 'h' for horizontal or 'v' for vertical.\n")
    try:
        orientation = input("Select Orientation: ")
        if orientation in ("h", "v"):
            return orientation
        else:
            print("\nThat's an interesting direction! Try again.")
    except ValueError:
        print("\nPlease enter either 'h' or 'v'")

    return orientation



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
    row_guess = computer_board.coords_guess("Row")
    col_guess = computer_board.coords_guess("Column")
    guess = row_guess, col_guess
    # computer_board.update_board(guess, *)
    # computer_board.print_board()
    orientation_guess = get_orientation()
    # player_logic_board = player_board.get_logic_board()
    # computer_logic_board = computer_board.get_logic_board()
    # print(player_logic_board)
    # print(computer_logic_board)
    # player_logic_board.update_ship(guess)
    # print(player_logic_board)
    carrier = Ship(6, orientation_guess, guess)
    carrier_coords = carrier.get_coords()
    print(carrier_coords)
    ship_row_guess = computer_board.coords_guess("Row")
    ship_col_guess = computer_board.coords_guess("Col")
    coord = {'row': ship_row_guess, 'col': ship_col_guess}
    computer_board.check_hit(carrier_coords, coord)
    computer_board.print_board()



game_loop()
