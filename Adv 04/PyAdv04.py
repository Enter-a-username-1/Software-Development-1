# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 04
 ------------------------------------------------------
  Date: 3-9-2026

  Partners:
  Name 1: Kael Secrest
  Detailed Contributions:
      Wrote the validation functions and the spots that ask for user input.
      I also helped with the bug testing.
      Finally I also wrote the closing stats (accuracy, shots fired, etc.) to match the real game.

  Name 2: William Rainey
  Detailed Contributions:
      I wrote the main narrative text and helped with the formatting of the output. 
      I also helped test the main code to ensure there were no bugs.
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do.
    2. Be sure to use comments and follow our coding standards.
        * Enough to explain why you are doing what you are doing.
        * Don't forget Docstrings on EVERY function.
    3. Imports and constants appear directly below the header.
    4. Use descriptive variable names. All caps for constants only.
    5. Function definitions come right after constants.
    6. Use TEST_SIGNALS to test functions and then run INTERCEPTED_SIGNALS.
    7. Don't forget to add your names and contributions.
       Include details of who did what, not just "partner 1 did part 1".

"""

###################################################################################################
# ------------------ Part 1: Imports and Constants ----------------------------
###################################################################################################
# Imports.  Only import libraries if you are going to use them.
import random

# Constants.  Make sure they are ALLCAPS.
INTERNNAME = "John Helldiver"
CORRECT_ID_LEN = 11

# 2 valid, 2 invalid, 3 spoofed, 1 corrupt
TEST_SIGNALS = [
    "51234543210",  # VALID: Sector 5 Sum: 30 checksum: 0
    "23891219836",  # VALID: Sector 2 Sum: 46 checksum: 6
    "999999",       # INVALID (too short)
    "4567845678456",  # INVALID (too long)
    "91827364505",  # SPOOFED id not mirrored
    "55555555551",  # SPOOFED invalid checksum 0
    "10101010105",  # SPOOFED sectors invalid
    "SIGNAL_TEST"   # CORRUPTED (Non-numeric)
]


INTERCEPTED_SIGNALS = [
    "32243334228", "62345678905", "42998489924", "LYRA__GHOST",
    "07731013776", "34288387248", "61224642210", "4321", "86734843766",
    "22424242420", "COMING_4YOU", "93699699638", "5432151234", "04539093542",
    "5555555555555", "14387178346", "C_K_IS_MINE", "4321432143213", "88888888881"
]


###################################################################################################
# ------------------ Part 2: Function Definitions ----------------------------
###################################################################################################
# TODO: Implement functions with docstrings

# --- Function 2A: is_number Function ---

def is_number(id_string):
    """
    Determine whether a supplied ID contains only numeric digits.
    Parameters:
        id_string - The ID value to inspect.
    Returns:
        True if every character is numeric, otherwise False.
    """
    return id_string.isdigit()


# --- Function 2B: is_correct_len Function ---

def is_correct_len(id_string, correct_length):
    """
    Compare an ID length to an expected length.
    Parameters:
        id_string - The ID value to inspect.
        correct_length - Required length of the ID.
    Returns:
        "correct" when exact length, "short" when too short, or "long" when too long.
    """
    if len(id_string) == correct_length:
        return "correct"
    if len(id_string) < correct_length:
        return "short"
    return "long"


# --- Function 2C: is_valid_sector Function ---

def is_valid_sector(id_string):
    """
    Verifies sector number appears in sector positions.
    Parameters:
        id_string - The numeric ID value to inspect.
    Returns:
        True if the sector digit at index 0 matches index 5, otherwise False.
    """
    if len(id_string) < 6:
        return False

    return id_string[0] == id_string[5]


# --- Function 2D: is_valid_tempid Function ---

def is_valid_tempid(id_string):
    """
    Verifies the first temp ID block mirrors the second temp ID block in reverse.
    Parameters:
        id_string - The numeric ID value to inspect.
    Returns:
        True if temp ID is mirrored correctly, otherwise False.
    """
    if len(id_string) < 10:
        return False

    first_temp_block = id_string[1:5]
    second_temp_block = id_string[6:10]
    return first_temp_block == second_temp_block[::-1]


# --- Function 2E: is_valid_checksum Function ---

def is_valid_checksum(id_string):
    """
    Verifies the checksum using the sum of the first 10 digits.
    Parameters:
        id_string - The numeric ID value to inspect.
    Returns:
        True if valid, else False.
    """
    running_total = 0

    for digit_char in id_string[:10]:
        running_total = running_total + int(digit_char)

    calculated_checksum = running_total % 10
    checksum_matches = calculated_checksum == int(id_string[10])
    return checksum_matches, calculated_checksum


# --- Function 2F: is_valid_id Function ---

def is_valid_id(id_string):
    """
    Determines whether an ID is valid and return either checksum or failure reason.
    Parameters:
        id_string - The ID value.
    Returns:
        True when ID is valid.
        False when ID is invalid.
    """
    if not is_number(id_string):
        return False, "string"
    length_result = is_correct_len(id_string, CORRECT_ID_LEN)
    if length_result == "short":
        return False, "too short"
    if length_result == "long":
        return False, "too long"
    if not is_valid_tempid(id_string):
        return False, "invalid tempid"
    if not is_valid_sector(id_string):
        return False, "invalid sectors"
    checksum_valid, checksum_value = is_valid_checksum(id_string)
    if not checksum_valid:
        return False, "invalid checksum"
    return True, checksum_value


###################################################################################################
# ------------------ Part 3: Main Code ----------------------------
###################################################################################################

# ------------------ Part 3A: Opening Narrative ----------------------------
# TODO: simple 5 sentence opening

coward = False
print(f"Dear Helldiver {INTERNNAME},")
print("There had been a rise in forged IDs by the automatons.")
print("The UGS had implemented a new validation tool for IDs.")
print("Unfortuantly , the tool is on a machine on a contoled planet called Tibit.")
print("Tibit recently became taken over by automatons"
" and has become a major hotspot of battle.")
print("We need you to analyze the intercepted IDs and classify them for us.")
print()
acceptMisson = input("PRESS Y TO ACCEPT THE MISSION ").upper()
if acceptMisson != "Y":
    print("Too bad you didn't have a choice")
    coward = True
print("LAUNCH INITIATED")
print("When you land on Tibit you will have to find the machine and copy the code to" \
" your Personal Hellpad system. Then you can run the code and analyze the intercepted IDs.")
print("Good luck Helldiver")
print()
startCopy = input("You have made it to the machine, start copy (Y/N)?")
while startCopy != "Y":
    print("You have to copy the code to complete mission.")
    startCopy = input("Start copy? (Y/N)").upper()
print("Copying code and running analysis...")

# ------------------ Part 3B: Test ID List ----------------------------
# TODO: use functions above to test validity of each given ID
# TODO: create valid_ids, spoofed_ids and corrupted_data lists

valid_ids = []
invalid_ids = []
spoofed_ids = []
corrupted_data = []

for signal_id in INTERCEPTED_SIGNALS:
    is_valid, result = is_valid_id(signal_id)

    if is_valid:
        valid_ids.append(signal_id)
    elif result == "string":
        corrupted_data.append(signal_id)
    elif result == "too short" or result == "too long":
        invalid_ids.append(signal_id)
    else:
        spoofed_ids.append(signal_id)

spoofed_ids.sort()
corrupted_data.sort()


# ------------------ Part 3C: Display ID stats ----------------------------
# TODO: Display len of each list
# TODO: Display sorted spoofed values

print("=" * 100)
print("The Personal Hellpad System has processed the " \
"intercepted signals and classified them as follows:")
print("=" * 100)
print()
print(f"   ✅ VALID HIL IDs:    {len(valid_ids):>2}")
print(f"   ❌ INVALID IDS:      {len(invalid_ids):>2}")
print(f"   👿 SPOOFED IDS:      {len(spoofed_ids):>2}")
print(f"   ⚠️  CORRUPTED DATA:  {len(corrupted_data):>2}")
print()
print("   🪪  Spoofed IDs: ", end="")
for spoofed_id in spoofed_ids:
    print(spoofed_id, end=" ")
print()
print()


# ------------------ Part 3D: Display Corrupted IDs ----------------------------
# TODO: Display corrupted IDs as part of narrative

print("RETURN TO THE PELICAN FOR EXTRACTION")
sideMission = input("Do you decide to do side mission of launch ICBM (Y/N)?").upper()
if sideMission == "Y":
    print("Launching ICBM...")
    print("The ICBM has been launched and is on its way to the target.")
    print("(Explosion sound effect)")
    print("The explosion has caused a shockwave that has disrupted the automaton's communication systems.")
    print("This has given us a temporary advantage in the battle for Tibit.")

if coward == True:
    print("Im suprised a coward like you made it this far, but here we are.")
else:
    print("Congratulations on making it this far, " \
    "but now we have to deal with the corrupted data.")
print("By lining up these spoofed IDs, we can see a message being written out.")
print()
print("The automotons are saying something.")
print()

for corrupted_id in corrupted_data:
    print(f"    {corrupted_id}")

print()


# ------------------ Part 3E: Closing Narrative ----------------------------
# TODO: simple 2-3 sentence closing

print("Who the hell(diver) is Lyra and why is she a ghost?")
print()
print("=" * 100)
if coward == True:
    if sideMission == "Y":
        print("MISSION COMPLETE")
        print("⭐⭐")
        print("Disgraceful conduct")
    else:
        print("MISSION COMPLETE")
        print("⭐")
        print("Cowardly conduct")
else:
    if sideMission == "Y":
        print("MISSION COMPLETE")
        print("⭐⭐⭐⭐")
        print("Heroic conduct")
    else:
        print("MISSION COMPLETE")
        print("⭐⭐⭐")
        print("Brave conduct")
print(f"Kills: {random.randint(0, 1000)}")
print(f"Accuracy: {random.randint(20, 60)}%")
print(f"Shots fired: {random.randint(500, 1000)}")
print(f"Shots hit: {random.randint(0, 500)}")
print(f"STIMS used: {random.randint(0, 26)}")
print(f"Accidentals: {random.randint(0, 15)}")
print(f"Samples Extracted: {random.randint(0, 100)}")
print(f"Stratagems used: {random.randint(0, 50)}")
print(f"Melee kills: {random.randint(0, 23)}")
print(f"Friendly fire damage dealt: {random.randint(0, 1000)}")
print("=" * 100)