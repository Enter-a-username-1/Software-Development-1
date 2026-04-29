# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 06C 
 ------------------------------------------------------
  Date:

  Partners:
  Name 1: Kael Secrest
  Detailed Contributions:   

  Name 2: Will 
  Detailed Contributions: 
   
      
      
  Tips:
    1. Start early. Come to the Help Sessions if you have problems
    2. Use full Docstrings with description, parameters, returns and example for all functions
    3. Write at least 10 taunts total
    4. Test the functions as you write them.  Do not trust them until tested
    5. Validate your coordinate input
    6. Write your 3 IDEAS at the bottom
      
"""
###################################################################################################
# ------------------ Part 1: Imports and Constants ----------------------------
###################################################################################################
# Imports.  Only import libraries if you are going to use them
import numpy as np
import random
import os

# --- Constants ---
MAX_TURNS = 10
MAX_DAMAGE = 100.0
DAMAGE_DECOY = 33.5
GRID_SIZE = 10
MAP_FILE = "sector_map.csv"
TAUNTS_FILE = "taunts.txt"
LOG_FILE = "log.txt"
INTERN_NAME = "John Helldiver"


###################################################################################################
# ------------------ Part 2: Function Definitions ----------------------------
###################################################################################################
def read_numpy_data(filename, delim, datatype):
    """
    ---- PROVIDED BY PROFESSOR - DO NOT MODIFY ----
    This function reads data file into a 1D NumPy array of ints

    Parameters: 
        str -> filename
        str -> delim - delimiter character
        str -> datatype
    Return:
        nd array of ints or None if an error occurs
    Example:
        full_map = read_numpy_data(FILENAME, " ", str)
    """
    import os

    # change directory to same as the program save location
    try:
        os.chdir(os.path.dirname(__file__))

    except Exception as e:
        # if error, try Jupyter notebook method
        print(f"   Error: {e}.  Trying Jupyter notebook method")
        
        os.chdir(os.path.dirname(globals()["__vsc_ipynb_file__"]))

    # load data from filename into numpy array
    try:
        array = np.loadtxt(filename, delimiter=delim, dtype=datatype)
        print(f"{filename} successfully read into NumPy array")
    except Exception as e:
        print("Error:", e)
        return None
    else:
        return array
    

# ------------------ Part 2A ----------------------------
# TODO: Add AI function read_text_file from LAB6B here
def read_text_file(filename):
    """
    Read a text file and return its lines as a stripped tuple of strings.

    Parameters:
        filename (str): Name of the text file to read.

    Returns:
        tuple: Tuple of stripped, non-empty strings from the file,
               or an empty tuple if an error occurs.

    Example:
        taunts = read_text_file("taunts.txt")
    """
    try:
        with open(filename, 'r') as f:
            lines = tuple(line.strip() for line in f if line.strip())
        return lines
    except Exception as e:
        print(f"   An error occurred {e}")
        return tuple()


# ------------------ Part 2B ----------------------------
# TODO: Add AI function count_adjacent from Lab6B here
def count_adjacent(grid, row, col):
    """
    Count non-empty cells in the 8 positions adjacent to a grid coordinate.

    Parameters:
        grid (numpy.ndarray): 2D integer grid (0=empty, 1=decoy, 2=scientist).
        row (int): Row index of the cell to check around.
        col (int): Column index of the cell to check around.

    Returns:
        int: Number of adjacent cells with a non-zero value.

    Example:
        adj = count_adjacent(sector_map, 3, 4)
    """
    count = 0
    rows, cols = np.shape(grid)

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:

            # Skip the cell itself
            if dr == 0 and dc == 0:
                continue

            r, c = row + dr, col + dc

            # Check bounds then count if non-empty
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] != 0:
                    count += 1

    return count


# ------------------ Part 2C ----------------------------
# TODO: Write function to display map with rows and column numbers
def display_map(reveal_grid):
    """
    Print the player's revealed map with row and column number headers.

    Parameters:
        reveal_grid (list): 2D list of strings representing the map state.
                            '-' = hidden, 'X' = decoy, 'L' = scientist,
                            digit string = adjacent count.

    Returns:
        None

    Example:
        display_map(reveal_grid)
    """
    # Column header row
    print(f"{'':11}", end="")
    for col in range(GRID_SIZE):
        print(f"{col:4}", end="")
    print()

    # Separator line
    print(f"{'':8}" + "-" * (GRID_SIZE * 4 + 1))

    # Data rows with row numbers
    for row in range(GRID_SIZE):
        print(f"{row:6} |", end="")
        for col in range(GRID_SIZE):
            print(f"{reveal_grid[row][col]:>4}", end="")
        print()


#------------------ Part 2D ----------------------------
# TODO: Write function to validate row,col
def parse_input(user_input):
    """
    Parse and validate a 'row,col' coordinate string.

    Parameters:
        user_input (str): Raw string input from the user (e.g. '3, 7').

    Returns:
        tuple: (row, col) as integers if valid and in range,
               or (-1, -1) if input is malformed or out of bounds.

    Example:
        row, col = parse_input("5, 6")  # returns (5, 6)
        row, col = parse_input("13,19") # returns (-1, -1)
    """
    try:
        parts = user_input.strip().split(',')
        if len(parts) != 2:
            return (-1, -1)

        row = int(parts[0].strip())
        col = int(parts[1].strip())

        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            return (row, col)
        else:
            return (-1, -1)

    except Exception:
        return (-1, -1)


#------------------ Part 2E ----------------------------
# TODO: Write function to write to log file
def write_log(filename, message):
    """
    Append a single message line to the specified log file.

    Parameters:
        filename (str): Path/name of the log file to write to.
        message  (str): The message string to append.

    Returns:
        None

    Example:
        write_log("log.txt", "NEW GAME - Turns left: 10 - Damage 0%")
    """
    try:
        with open(filename, 'a') as f:
            f.write(message + '\n')
    except Exception as e:
        print(f"Log error: {e}")


###################################################################################################
# ------------------ Part 3: Main Code ----------------------------
###################################################################################################

# ------------------ Part 3A: Reading Files ----------------------------
sector_map = read_numpy_data(MAP_FILE, " ", int)
taunts     = read_text_file(TAUNTS_FILE)

# Exit early if either file failed to load
if sector_map is None:
    print("Error: Could not load sector map. Exiting.")
    exit()

if len(taunts) == 0:
    print("Error: Could not load taunts file. Exiting.")
    exit()

# Build the revealed grid — all cells start hidden
reveal_grid = [['-'] * GRID_SIZE for _ in range(GRID_SIZE)]


# ------------------ Part 3B: Opening Narrative ----------------------------
# TODO: simple 5 sentence opening
print("""
    After a long ship ride through the sector, you finally lock onto Lyra's signal.
    You are super close to finding her.
    Super Earth is counting on you to find her and bring her back safely.
    Lyra is a brilliant scientist and she is anti-democracy.
    Bring her to justice and help Super Earth win the war agenst the Automotauns.
    Help fly your Destroyer to the right location.
""")
input("\nPress ENTER to continue\n")


# ------------------ Part 3C: Game Loop ----------------------------
# TODO: loop through the number of turns, get guess coordinates, display map
turns_left = MAX_TURNS
damage = 0.0
game_over = False
found_scientist = False
out_of_turns = False
too_much_damage = False

# Log the start of the game
write_log(LOG_FILE, f"NEW GAME - Turns left: {turns_left} - Damage {damage}%")

while not game_over:

    # Display the current revealed map and turn count
    print(f"\n   Revealed Map: Turns remaining {turns_left}\n")
    display_map(reveal_grid)

    # Print a random taunt from the file
    taunt = random.choice(taunts)
    print(f"\nLyra: {taunt}\n")

    # Keep prompting until we get a valid, un-guessed coordinate
    while True:
        user_input = input("Enter the row, col of your guess (row,col): ")
        row, col = parse_input(user_input)

        # Reject out-of-range or malformed input
        if row == -1:
            print(f"INVALID: {user_input.strip()}. ", end="")
            continue

        # Reject coordinates that have already been revealed
        if reveal_grid[row][col] != '-':
            print("That location was tried already.  Try again")
            continue

        break  # Valid, un-guessed coordinate found

    # Decrement turns after a valid guess
    turns_left -= 1
    cell_value = int(sector_map[row][col])

    if cell_value == 0:
        # Empty cell — reveal adjacent count
        adj = count_adjacent(sector_map, row, col)
        reveal_grid[row][col] = str(adj)
        print(f"\nThat location has {adj} adjacent items")
        write_log(
            LOG_FILE,
            f"{row},{col} - Turns left: {turns_left} - Damage {damage}% - {adj} adjacent"
        )

    elif cell_value == 1:
        # Decoy — deal hull damage
        reveal_grid[row][col] = 'X'
        damage += DAMAGE_DECOY
        print(f"\n💥 Decoy! Hull damage {damage}%")
        write_log(
            LOG_FILE,
            f"{row},{col} - Turns left: {turns_left} - Damage {damage}% - Decoy hit"
        )

        if damage >= MAX_DAMAGE:
            too_much_damage = True
            game_over = True

    elif cell_value == 2:
        # Scientist found — player wins
        reveal_grid[row][col] = 'L'
        found_scientist = True
        game_over = True
        print("\n Helldiver we have her locked in. Lyra is there")
        write_log(
            LOG_FILE,
            f"{row},{col} - Turns left: {turns_left} - Damage {damage}% - Lyra found"
        )

    # Check if the player has run out of turns
    if turns_left <= 0 and not game_over:
        out_of_turns = True
        game_over = True


# ------------------ Part 3D: Closing Narrative ----------------------------
# TODO: create three closings:
# 1. One for when the turns runs out
# 2. One for when lives run out
# 3. One for when the scientist is found
if found_scientist:
    write_log(LOG_FILE, f"Success: Turns left: {turns_left} - Damage {damage}%")
    print("""
    Well done Helldiver. You have captured Lyria and she will face justice
    for her crimes against democracy. Super Earth is grateful for your service.
    We are promoting you to the rank of Captain. Congrats.
    """)

elif too_much_damage:
    write_log(
        LOG_FILE,
        f"Failure: Ship destroyed - Damage {damage}% - Turns left: {turns_left}"
    )
    print("""
    Helldiver, the mission was not a success. Your ship has taken too much damage and is no longer operational.
    Lyra has evaeded us and we are now stuck in space will the next transport ship to arrive.
    We have made the reggretful decision to discharge you from the Helldivers.
    Your new rank is Janitor. Good luck in your future endeavors.
    """)

else:
    write_log(LOG_FILE, f"Failure: Out of turns - Damage {damage}%")
    print("""
    We have uncomfirmed reports that Lyra has escaped the sector.
    We are not sure how she escaped but we are sure that it was your fault.
    We are demoting you to the rank of Private and you will be assigned to janitorial
    duties. We wish you well in your future endeavors.
    """)


# ------------------ Part 4: IMPROVEMENTS ----------------------------
# TODO: What are 3 ideas for improvements to the functionality of this lab?
# How difficult would it be to write the code for this?
"""
1. Difficulty levels (Easy / Medium / Hard) - not too hard

2. A hint system -  mildy difficult

3. Diffrent ranks for how quickly you find Lyra and how much damage you take. - pretty easy

"""
