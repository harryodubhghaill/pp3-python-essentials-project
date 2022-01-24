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

    def get_coords(self, board_size):
        if self.orientation == 'h':
            if self.start['row'] in range(board_size):
                coordinates = []
                for index in range(self.boat_size):
                    if self.start['col'] + index in range(board_size):
                        coordinates.append({'row': self.start['row'],
                                            'col': self.start['col'] + index})
                    else:
                        raise IndexError("Column is out of range.")
                return coordinates
            else:
                raise IndexError("Row is out of range.")
        elif self.orientation == 'v':
            if self.start['row'] in range(board_size):
                coordinates = []
                for index in range(self.boat_size):
                    if self.start['col'] + index in range(board_size):
                        coordinates.append({'row': self.start['row'] + index,
                                            'col': self.start['col']})
                    else:
                        raise IndexError("Row is out of range.")
                return coordinates
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

    def print_board(self):
        """
        Takes size and name from class to print styled and indexed play
        board.
        """
        print(self.title)
        print("\n  " + " ".join(str(x) for x in range(1, self.size + 1)))
        for r in range(self.size):
            print(str(r + 1) + " " + " ".join(str(y) for y in self.board[r]))

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
        print(guess)
        for coord in guess:
            print(coord)
            print('hello')
            self.board[coord['row']][coord['col']] = f'{symbol}'

        print(f"{self.name}'s board updated")

    def check_hit(self, ship_coords, guess_coords):
        if guess_coords in ship_coords:
            self.update_board(guess_coords, 'X')
            print("Hit!")
        else:
            self.update_board(guess_coords, 'O')
            print("Miss!")

        print(guess_coords)


# utility function to clear terminal
def clear_term():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # check for os
        command = 'cls'
    os.system(command)


def print_start():
    print(("~"*50)+"\n"+("~"*50))
    print("~~~~~~     WELCOME TO BATTLESHIP ROYAL      ~~~~~~")
    print("~~  OBJECTIVE: TOTAL DESTRUCTION OF YOUR ENEMY  ~~")
    print(("~"*50)+"\n"+("~"*50))
    print("** HOW TO PLAY **/n")
    print("Type your name into the field below")
    print("Select your Difficulty")
    print("Place your ships")
    print("Fire missiles at your opponents ships")
    print("Winner is first to clear all enemy ships")


def get_name():
    player_name = input("Please enter your name: ")
    print(f"\nWelcome to the game {player_name}")
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


def board_init(difficulty, name):
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
    print("\nChoose Ship Orientation.")
    print("\nType 'h' for horizontal or 'v' for vertical.\n")
    while True:
        try:
            orientation = input("Select Orientation: ")
            if orientation in ("h", "v"):
                return orientation
            else:
                print("\nThat's an interesting direction! Try again.")
        except ValueError:
            print("\nPlease enter either 'h' or 'v'")


def game_init():
    clear_term()
    print_start()


def get_guess(board):
    row_guess = board.coords_guess("Row")
    col_guess = board.coords_guess("Column")
    guess = {'row': row_guess, 'col': col_guess}
    return guess


def get_ship_info(board):
    while True:
        try:
            orientation_guess = get_orientation()
            guess = get_guess(board)
            board_size = board.size
            carrier = Ship(4, orientation_guess, guess)
            carrier_coords = carrier.get_coords(board_size)
            break
        except IndexError:
            print("Your ship aint gonna fit there bud")
            print("Try again")
    return carrier_coords
#  Ship instance definitions
#  battleship = Ship(5, orientation_guess, guess)
#  cruiser = Ship(4, orientation_guess, guess)
#  destroyer = Ship(3, orientation_guess, guess)
#  patrol_boat = Ship(2, orientation_guess, guess)
#  scuba_spy = Ship(1, orientation_guess, guess)


def game_loop():
    game_init()
    player_name = get_name()
    difficulty = choose_difficulty()
    player_board = board_init(difficulty, player_name)
    computer_board = board_init(difficulty, "Computer")
    player_board.print_board()
    computer_board.print_board()
    carrier_coords = get_ship_info(computer_board)
    computer_board.update_board(carrier_coords, '@')
    computer_board.print_board()
    # coord = get_guess(computer_board)
    # computer_board.check_hit(carrier_coords, coord)
    # computer_board.print_board()
    # computer_board.update_board(guess, *)
    # computer_board.print_board()
    # player_logic_board = player_board.get_logic_board()
    # computer_logic_board = computer_board.get_logic_board()
    # print(player_logic_board)
    # print(computer_logic_board)
    # player_logic_board.update_ship(guess)
    # print(player_logic_board)


game_loop()
