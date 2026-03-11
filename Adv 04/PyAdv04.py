# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 04
 ------------------------------------------------------
  Date: 3-9-2026

  Partners:
  Name 1: Kael Secrest
  Detailed Contributions:
      Wrote helper validation functions and built the ID classification loop.
      Added formatted output sections and tested category counts with provided data.

  Name 2: [Add Partner Name]
  Detailed Contributions:
      Add your partner's specific contributions before submission.

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

# Helper functions used to validate and classify IDs.


# --- Function 2A: is_number Function ---

def is_number(id_string):
    """
    Determine whether a supplied ID contains only numeric digits.

    Parameters:
        id_string (str): The ID value to inspect.

    Returns:
        bool: True if every character is numeric, otherwise False.
    """
    return id_string.isdigit()


# --- Function 2B: is_correct_len Function ---

def is_correct_len(id_string, correct_length):
    """
    Compare an ID length to an expected length.

    Parameters:
        id_string (str): The ID value to inspect.
        correct_length (int): Required length of the ID.

    Returns:
        str: "correct" when exact length, "short" when too short, or "long" when too long.
    """
    if len(id_string) == correct_length:
        return "correct"

    if len(id_string) < correct_length:
        return "short"

    return "long"


# --- Function 2C: is_valid_sector Function ---

def is_valid_sector(id_string):
    """
    Verify sector number appears in both required sector positions.

    Parameters:
        id_string (str): The numeric ID value to inspect.

    Returns:
        bool: True if the sector digit at index 0 matches index 5, otherwise False.
    """
    if len(id_string) < 6:
        return False

    return id_string[0] == id_string[5]


# --- Function 2D: is_valid_tempid Function ---

def is_valid_tempid(id_string):
    """
    Verify the first temp ID block mirrors the second temp ID block in reverse.

    Parameters:
        id_string (str): The numeric ID value to inspect.

    Returns:
        bool: True if temp ID is mirrored correctly, otherwise False.
    """
    if len(id_string) < 10:
        return False

    first_temp_block = id_string[1:5]
    second_temp_block = id_string[6:10]
    return first_temp_block == second_temp_block[::-1]


# --- Function 2E: is_valid_checksum Function ---

def is_valid_checksum(id_string):
    """
    Validate checksum using sum of first 10 digits modulo 10.

    Parameters:
        id_string (str): The numeric ID value to inspect.

    Returns:
        tuple: (True, calculated_checksum) if valid, else (False, calculated_checksum).
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
    Determine whether an ID is valid and return either checksum or failure reason.

    Parameters:
        id_string (str): The ID value to validate.

    Returns:
        tuple:
            (True, checksum) when ID is valid.
            (False, reason) when ID is invalid.

        Reasons are limited to:
            "non-numeric", "too short", "too long",
            "invalid tempid", "invalid sectors", "invalid checksum"
    """
    if not is_number(id_string):
        return False, "non-numeric"

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


# Opening narrative text.
print("QUACK's status light flickers as the beacon panel fills with red warning markers.")
print("I lean in and ask for the Lyra trace while static hisses through the channel.")
print("QUACK flags multiple forged IDs and says the pattern looks intentional.")
print("This is Helldiver-level signal triage: classify fast, strike faster.")
print("For Super Earth, we clean this list before Lyra reaches C.K.")
print()


# ------------------ Part 3B: Test ID List ----------------------------
# TODO: use functions above to test validity of each given ID
# TODO: create valid_ids, spoofed_ids and corrupted_data lists


# Process intercepted IDs and classify each one.
valid_ids = []
invalid_ids = []
spoofed_ids = []
corrupted_data = []

for signal_id in INTERCEPTED_SIGNALS:
    is_valid, result = is_valid_id(signal_id)

    if is_valid:
        valid_ids.append(signal_id)
    elif result == "non-numeric":
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


# Display mission statistics.
print("=" * 80)
print("    QUACK: 'Scanning complete! Let's see what we caught in the net.'")
print("=" * 80)
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


# Display corrupted IDs one per line.
print("QUACK: Great tail-feathers! You found Lyra's fakes.")
print("By isolating these spoofed IDs, we can trace the signal origin.")
print()
print("Wait... look at the corrupted data list.")
print()

for corrupted_id in corrupted_data:
    print(f"    {corrupted_id}")

print()


# ------------------ Part 3E: Closing Narrative ----------------------------
# TODO: simple 2-3 sentence closing


# Short ending story text.
print("QUACK: 'She's taunting us!'")
print("I mark the spoof source and prep a hot drop like a Helldiver on final approach.")
print("Lyra has a lead, but now we have her trail.")
