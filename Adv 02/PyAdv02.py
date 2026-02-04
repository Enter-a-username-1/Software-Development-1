# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 02 
 ----------------------------
  Date:2/2/2026

  Partner 1 Name: Kael Secrest
  Partner 1 Contributions: Code Parts 1, 2

  Partner 2 Name: 
  Partner 2 Contributions: 
   
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Be sure to use comments and follow our coding standards.
        * Not too many comments but enough to explain what you are doing.
        * There are some comments for you to follow but add your own
    3. Imports and Constants at the top
    4. Use descriptive variable names
    5. Display calculations with units
    6. Do not let any lines (code or comments) go past 99 characters wife
    7. Make sure your table output lines up
    8. Rerun the code and test the output with different input values before submitting
    9. DO NOT copy/paste from websites or GenAI.  Do your own work and understand your code
      
"""
# ------------------ Part 1: Imports and Constants ----------------------------
# TODO: Imports
import math

# TODO: Constants.  Make sure the variables are ALLCAPS
INTERN = "John Helldiver"
COMPANYNAME = "Galatic United States"
INTERNID = "998877"
BEACON_ID = "Eagle-2132"

# ------------------ Part 2: Introductory Narrative ----------------------------
# TODO: Display a short 3-5 sentence introduction

#checks badge ID
input_id = input("Enter your GUS Badge ID: ")
if input_id != INTERNID:
  print("Badge ID not recognized. Access denied.")
  print("Try again")
  input_id = input("Enter your GUS Badge ID: ")
  if input_id != INTERNID:
    print("Badge ID not recognized. Access denied.")
    print("Try again")
    input_id = input("Enter your GUS Badge ID: ")
    if input_id != INTERNID:
      print("You know what fine close enough.")

#Story intro
print(f"Badge ID {input_id} accepted. Welcome to the {COMPANYNAME} orbital beacon troubleshooter.")
print(f"Hello intern {INTERN}, and your task is to analyze incoming beacon data.")
print("")
print("HR has left you the following note:")
print(f"We need help analyzing the beacon data from {BEACON_ID} that is currently orbiting Melevlon Creek.")
print("Soldiers on the battlefiled below need the beacon to find their location on their Galactic War Map.")

# ------------------ Part 3: Drift Angle ----------------------------
# TODO: Calculate drift angle and determine drift status
print("")
print("To begin we need some infromation about the beacon from you.")

# input for velocity and time
horizontalOffset = float(input("Enter the horizontal offset of the beacon (in km): "))
verticalOffset = float(input("Enter the vertical offset of the beacon (in km): "))
driftAngle = math.degrees(math.atan2(verticalOffset, horizontalOffset))

# check if drift status is critical
if driftAngle < 10:
    driftStatus = "Acceptable"
elif 10 <= driftAngle <= 20:
    driftStatus = "Elevated"
elif 0 == driftAngle:
    driftStatus = "Beacon cannot be calculated"
    driftAngle = -99999
else:
    driftStatus = "Excessive"

# ------------------ Part 4: Signal Degradation ----------------------------
# TODO: Calculate degradation and determine signal status




# ------------------ Part 5: Beacon Report ----------------------------
# TODO: Print beacon report




# ------------------ Part 6: Closing Narrative ----------------------------
# TODO: Display 2-3 sentences wrapping up the lab story
print("Analysis complete. Beacon data has been logged and reported to the defense team.")
print("Orbitals and Galatic War Maps are back online and functioning within normal parameters.")
print("Good work, intern John Helldiver! You have successfully aided managed democracy.")



