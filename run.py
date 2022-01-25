from random import randint
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
    def __init__(self, size, name):
        self.size = size
        self.name = name

        self.title = f"{self.name}'s board"

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
                    print("\nAhh now, you'll never win the war from there")
            except ValueError:
                print("\nPlease enter a number")

    def update_board(self, guess, symbol):
        """
        Takes guess and updates board to reflect.
        """
        for coord in guess:
            self.board[coord[0]][coord[1]] = f'{symbol}'

    def check_hit(self, guess_coords, data_set):
        """
        Checks if missile (gueess_coords) hits
        enemy ship.
        Updates the board with visual marker and
        if missile hits, remove ship coordinate.
        """
        if guess_coords in data_set:
            self.update_board([guess_coords], 'X')
            print(f"\n{self.name}'s ship was hit!")
            data_set.remove(guess_coords)
        else:
            self.update_board([guess_coords], 'O')
            print(f"\n{self.name} avoided disaster!")


def clear_term():
    """
    Utility function to clear terminal.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # check for os
        command = 'cls'
    os.system(command)


def print_start():
    """
    Prints stylized strings introducing the game to terminal.
    """
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
    """
    Gets the players name through terminal input.
    """
    player_name = input("Please enter your name: ")
    print(f"\nWelcome to the game {player_name}")
    return player_name


def choose_difficulty():
    """
    Prompts player to select one of the difficulty modes.
    Checks user input and returns difficulty value.
    """
    print("\nChoose your difficulty!")
    print("\nEnter 'e' for Easy, 'm' for Medium, 'h' for Hard\n")

    while True:
        try:
            difficulty = input("Enter Difficulty Level: ")

            difficulty_options = ("e", "m", "h")
            if difficulty in difficulty_options:
                clear_term()
                return difficulty
            else:
                print("Sorry, that's not an accepted value! Please try again")
        except ValueError:
            print("Please try again.")


def board_init(difficulty, name):
    """
    Takes chosen difficulty and name and passes it to
    the Board class to create an instance
    """
    if difficulty == "e":
        generated_board = Board(5, name)
        return generated_board
    elif difficulty == "m":
        generated_board = Board(7, name)
        return generated_board
    elif difficulty == "h":
        generated_board = Board(9, name)
        return generated_board


def place_ships(difficulty, board):
    """
    Takes difficulty param to select list of ships.
    Board param is for where ships are to be placed.
    We call the get_ship_info func to create our
    ship instances and get list of coordinates.
    Coordinates are then used to update display board
    and print updated board to terminal.
    """
    if difficulty == "e":
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
        rescue_boat_coords = get_ship_info(board, 2, 'Rescue Boat')
        board.update_board(rescue_boat_coords, '@')
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
        submarine_coords = get_ship_info(board, 3, 'Submarine')
        board.update_board(submarine_coords, '@')
        board.print_board()
        patrol_boat_coords = get_ship_info(board, 2, 'Patrol Boat')
        board.update_board(patrol_boat_coords, '@')
        board.print_board()
        rescue_boat_coords = get_ship_info(board, 2, 'Rescue Boat')
        board.update_board(rescue_boat_coords, '@')
        board.print_board()
        scuba_spy_coords = get_ship_info(board, 1, 'Jeff')
        board.update_board(scuba_spy_coords, '@')
        board.print_board()
    else:
        print("Error")


def get_orientation():
    """
    Prompts player to choose orientation of ship.
    Checks user input and returns orientation value.
    """
    print("\nChoose Ship Orientation.")
    print("\nType 'h' for horizontal or 'v' for vertical.")
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
    """
    Clears terminal and prints start screen.
    """
    clear_term()
    print_start()


def get_guess(board):
    """
    Board param is for board we want to guess on.
    """
    row_guess = board.coords_guess("Row")
    col_guess = board.coords_guess("Column")
    guess = (row_guess, col_guess)
    return guess


def get_ship_info(board, boat_size, boat_name):
    """
    Creates instances of Ship Class.
    Calls funtions to get player inputs.
    Generates coordinates for each Ship instance.
    Checks for occupied cells.
    If instance coordinates unique, return instance coordinates.
    """
    print(f"\nPlace {boat_name}.")
    print(f"{boat_name} is {boat_size} units long.")
    while True:
        try:
            orientation_guess = get_orientation()
            guess = get_guess(board)
            clear_term()
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


def fire_missile(board, data_set, missile_coords, guessed):
    """
    Sends the missile coordinates to the check_hit method
    for the appropriate board.
    Updates the appropriate list of guessed values.
    Takes ship_coords of enemy ships.
    """
    board.check_hit(missile_coords, data_set)
    guessed.append(missile_coords)
    board.print_board()


def restart_game():
    input("Press enter to restart")
    game_loop()


def turn(player_board, computer_board):
    """
    Checks if there are filled coordinates left
    for player to hit, starts turn, checks same
    for computer, calls computer turn.
    Repeats until either list is empty.
    """
    while True:
        if comp_list_ship_coords:
            player_turn(computer_board)
            if list_ship_coords:
                comp_turn(player_board)
            else:
                print("Computer Wins")
                restart_game()
                break
        else:
            print("Player Wins")
            restart_game()
            break


def player_turn(board):
    """
    Funtion to get missile guess from player.
    Checks for duplicate guess and re-prompts
    player.
    Takes ship_coords to pass to check_hit.
    """
    while True:
        try:
            print("Ready the torpedos!")
            print("Where we sending this one, boss?")
            coord = get_guess(board)
            clear_term()
            if coord in guessed_values:
                raise IndexError
            else:
                fire_missile(board, comp_list_ship_coords, coord,
                             guessed_values)
                break
        except IndexError:
            clear_term()
            print("You Picked that one already")
            print("Try again")


def comp_turn(board):
    """
    Funtion to automate the computers guess.
    Checks for duplicate guess and retries until
    unique coords are found.
    """
    while True:
        try:
            data = random_parameters(board)
            coord = data[1]
            if coord in comp_guessed_values:
                raise IndexError
            else:
                fire_missile(board, list_ship_coords, coord,
                             comp_guessed_values)
                break
        except IndexError:
            print("trying again...")


def random_parameters(board):
    """
    Function to randomly generate positional parameters
    for computer ships.
    Board param taken to get access to instance variables.
    """
    orientation = 'h' if randint(0, 1) == 0 else 'v'
    coords = (randint(0, board.size - 1), randint(0, board.size - 1))
    return orientation, coords


def generate_coords(board, boat_size, boat_name):
    """
    Creates instances of Ship Class.
    Calls random_parameters func to pass
    params to Ship instance.
    Generates coordinates for each Ship instance.
    Checks for occupied cells.
    If instance coordinates unique, return instance coordinates.
    """
    while True:
        try:
            parameters = random_parameters(board)
            orientation_guess = parameters[0]
            guess = parameters[1]
            board_size = board.size
            ship = Ship(boat_size, orientation_guess, guess, boat_name)
            instance_coords = ship.get_coords(board_size)
            for instance_coord in instance_coords:
                if instance_coord in comp_list_ship_coords:
                    raise IndexError
                else:
                    comp_list_ship_coords.append(instance_coord)
            return instance_coords
        except IndexError:
            continue


def generate_ships(difficulty, board):
    """
    Takes difficulty param to select list of ships.
    Board param is for where ships are to be placed.
    We call the generate_coords func to randomly generate
    parameters.
    """
    if difficulty == "e":
        generate_coords(board, 4, 'Cruiser')
        generate_coords(board, 3, 'Destroyer')
        generate_coords(board, 2, 'Patrol Boat')
        generate_coords(board, 1, 'Jeff')
    elif difficulty == "m":
        generate_coords(board, 5, 'Battleship')
        generate_coords(board, 4, 'Cruiser')
        generate_coords(board, 3, 'Destroyer')
        generate_coords(board, 2, 'Patrol Boat')
        generate_coords(board, 2, 'Rescue Boat')
        generate_coords(board, 1, 'Jeff')
    elif difficulty == "h":
        generate_coords(board, 6, 'Carrier')
        generate_coords(board, 5, 'Battleship')
        generate_coords(board, 4, 'Cruiser')
        generate_coords(board, 3, 'Destroyer')
        generate_coords(board, 3, 'Submarine')
        generate_coords(board, 2, 'Patrol Boat')
        generate_coords(board, 2, 'Rescue Boat')
        generate_coords(board, 1, 'Jeff')
    else:
        print("Error")


#  global lists
guessed_values = []
comp_guessed_values = []
list_ship_coords = []
comp_list_ship_coords = []


def game_loop():
    """
    Calls all game functions in order.
    """
    game_init()
    player_name = get_name()
    difficulty = choose_difficulty()
    player_board = board_init(difficulty, player_name)
    player_board.print_board()
    computer_board = board_init(difficulty, "Computer")
    place_ships(difficulty, player_board)
    generate_ships(difficulty, computer_board)
    turn(player_board, computer_board)


game_loop()
