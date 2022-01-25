import os


class Ship():
    """
    Defines Ship class with properties for placement and methods
    to track position and status
    """
    def __init__(self, size, orientation, start_coord, boat_name):
        self.boat_size = size
        self.boat_name = boat_name
        if orientation == 'h' or orientation == 'v':  # value check
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'h' or 'v'.")

        self.start = start_coord

    def get_coords(self, board_size):
        if self.orientation == 'h':
            if self.start[0] in range(board_size):
                coordinates = []
                for index in range(self.boat_size):
                    if self.start[1] + index in range(board_size):
                        coordinates.append((self.start[0],
                                            self.start[1] + index))
                    else:
                        raise IndexError("Column is out of range.")
                return coordinates
            else:
                raise IndexError("Row is out of range.")
        elif self.orientation == 'v':
            if self.start[1] in range(board_size):
                coordinates = []
                for index in range(self.boat_size):
                    if self.start[0] + index in range(board_size):
                        coordinates.append((self.start[0] + index,
                                            self.start[1]))
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
            self.board[coord[0]][coord[1]] = f'{symbol}'

        print(f"{self.name}'s board updated")

    def check_hit(self, ship_coords, guess_coords, used):
        if guess_coords in used:
            print("\nYou guessed that one already.")
        else:
            if guess_coords in ship_coords:
                self.update_board([guess_coords], 'X')
                print("Hit!")
                list_ship_coords.remove(guess_coords)
            else:
                self.update_board([guess_coords], 'O')
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
    print("~~~**   HOW TO PLAY   **~~~")
    print("Select your Difficulty")
    print("Place your ships")
    print("Fire missiles at your opponents ships")
    print("Winner is first to clear all enemy ships")


def get_name():
    player_name = input("Please enter your name: ")
    print(f"\nWelcome to the game {player_name}")
    return player_name


def choose_difficulty():
    print("\nChoose your difficulty!")
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


def place_ships(difficulty, board):
    if difficulty == "e":
        cruiser_coords = get_ship_info(board, 4, 'Cruiser')
        board.update_board(cruiser_coords, '@')
        board.print_board()
        destroyer_coords = get_ship_info(board, 3, 'Destroyer')
        board.update_board(destroyer_coords, '@')
        board.print_board()
        # patrol_boat_coords = get_ship_info(board, 2, 'Patrol Boat')
        # board.update_board(patrol_boat_coords, '@')
        # board.print_board()
        # scuba_spy_coords = get_ship_info(board, 1, 'Jeff')
        # board.update_board(scuba_spy_coords, '@')
        # board.print_board()
    elif difficulty == "m":
        battleship_coords = get_ship_info(board, 5, 'Battleship')
        board.update_board(battleship_coords, '@')
        board.print_board()
        cruiser_coords = get_ship_info(board, 4, 'Cruiser')
        board.update_board(cruiser_coords, '@')
        board.print_board()
        destroyer_coords = get_ship_info(board, 3, 'Destroyer')
        board.update_board(destroyer_coords, '@')
        board.print_board()
        patrol_boat_coords = get_ship_info(board, 2, 'Patrol Boat')
        board.update_board(patrol_boat_coords, '@')
        board.print_board()
        scuba_spy_coords = get_ship_info(board, 1, 'Jeff')
        board.update_board(scuba_spy_coords, '@')
        board.print_board()
    elif difficulty == "h":
        carrier_coords = get_ship_info(board, 6, 'Carrier')
        board.update_board(carrier_coords, '@')
        board.print_board()
        battleship_coords = get_ship_info(board, 5, 'Battleship')
        board.update_board(battleship_coords, '@')
        board.print_board()
        cruiser_coords = get_ship_info(board, 4, 'Cruiser')
        board.update_board(cruiser_coords, '@')
        board.print_board()
        destroyer_coords = get_ship_info(board, 3, 'Destroyer')
        board.update_board(destroyer_coords, '@')
        board.print_board()
        patrol_boat_coords = get_ship_info(board, 2, 'Patrol Boat')
        board.update_board(patrol_boat_coords, '@')
        board.print_board()
        scuba_spy_coords = get_ship_info(board, 1, 'Jeff')
        board.update_board(scuba_spy_coords, '@')
        board.print_board()
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
    guess = (row_guess, col_guess)
    return guess


list_ship_coords = []


def get_ship_info(board, boat_size, boat_name):
    print(f"Place your {boat_name}.")
    print(f"Your {boat_name} is {boat_size} units long.")
    while True:
        try:
            orientation_guess = get_orientation()
            guess = get_guess(board)
            board_size = board.size
            ship = Ship(boat_size, orientation_guess, guess, boat_name)
            instance_coords = ship.get_coords(board_size)
            for instance_coord in instance_coords:
                if instance_coord in list_ship_coords:
                    raise IndexError
                else:
                    list_ship_coords.append(instance_coord)
            return instance_coords
        except IndexError:
            print("Your ship aint gonna fit there bud")
            print("Try again")


guessed_values = []


def fire_missile(board, ship_coords):
    while True:
        if ship_coords:
            print(ship_coords)
            coord = get_guess(board)
            board.check_hit(ship_coords, coord, guessed_values)
            guessed_values.append(coord)
            board.print_board()
            print(ship_coords)
        else:
            print("game over")
            break


def game_loop():
    game_init()
    player_name = get_name()
    difficulty = choose_difficulty()
    player_board = board_init(difficulty, player_name)
    computer_board = board_init(difficulty, "Computer")
    player_board.print_board()
    computer_board.print_board()
    place_ships(difficulty, player_board)
    fire_missile(player_board, list_ship_coords)
    # computer_board.print_board()
    # computer_board.update_board(guess, *)


game_loop()
