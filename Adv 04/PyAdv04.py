# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 04
 ------------------------------------------------------
  Date:3-4-2026
  
  Partners:
  Name 1:Kael Secrest
  Detailed Contributions:   

  Name 2:
  Detailed Contributions: 
   
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Be sure to use comments and follow our coding standards.
        * Enough to explain why you are doing what you are doing.
        * Don't forget Docstrings on EVERY function
    3. Imports and constants appear directly below the header
    4. Use descriptive variable names.  All caps for constants only
    5. Function definitions come right after constants
    6. Use the TEST_SIGNALS to test your functions, make sure it runs with INTERCEPTED_SIGNALS
    7. Don't forget to add your names and contributions
       Include details of who did what, not just "partner 1 did part 1"

      
"""
###################################################################################################
# ------------------ Part 1: Imports and Constants ----------------------------
###################################################################################################
# Imports.  Only import libraries if you are going to use them
import random


# Constants.  Make sure they are ALLCAPS
INTERNNAME = "John Helldiver"


# 2 valid, 2 invalid, 3 spoofed, 1 corrupt
TEST_SIGNALS = [
    "51234543210",  # VALID: Sector 5 Sum: 30 checksum: 0
    "23891219836",  # VALID: Sector 2 Sum: 46 checksum: 6
    "999999",       # INVALID (too short)
    "4567845678456",# INVALID (too long)
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




# --- Function 2B: is_correct_len Function ---




# --- Function 2C: is_valid_sector Function ---




# --- Function 2D: is_valid_tempid Function ---




# --- Function 2E: is_valid_checksum Function ---




# --- Function 2F: is_valid_id Function ---

    


###################################################################################################
# ------------------ Part 3: Main Code ----------------------------
###################################################################################################

# ------------------ Part 3A: Opening Narrative ----------------------------
# TODO: simple 5 sentence opening




# ------------------ Part 3B: Test ID List ----------------------------
# TODO: use functions above to test validity of each given ID
# TODO: create valid_ids, spoofed_ids and corrupted_data lists





# ------------------ Part 3C: Display ID stats ----------------------------
# TODO: Display len of each list
# TODO: Display sorted spoofed values




# ------------------ Part 3D: Display Corrupted IDs ----------------------------
# TODO: Display corrupted IDs as part of narrative



# ------------------ Part 3E: Closing Narrative ----------------------------
# TODO: simple 2-3 sentence closing



