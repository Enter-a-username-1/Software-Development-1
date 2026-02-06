# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 02 
 ----------------------------
  Date:2/2/2026

  Partner 1 Name: Kael Secrest
  Partner 1 Contributions: Code Parts 2, 3, 5

  Partner 2 Name: Will Rainey
  Partner 2 Contributions: Code Parts 1, 4, 6
   
      
      
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
INTERNID = "5123454321"
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
print(f"We need help analyzing the beacon data from {BEACON_ID}")
print(f"The Beacon {BEACON_ID} is currently orbiting Melevlon Creek.")
print("Soldiers on the battlefiled below need infomation from the beacon.")
print("This is so they can find their location on their Galactic War Map.")

# ------------------ Part 3: Drift Angle ----------------------------
# TODO: Calculate drift angle and determine drift status
print("")
print("To begin we need some infromation about the beacon from you.")

# input for velocity and time
horizontalOffset = float(input("Enter the horizontal offset of the beacon (in km): "))
verticalOffset = float(input("Enter the vertical offset of the beacon (in km): "))
driftAngle = math.degrees(math.atan2(verticalOffset, horizontalOffset))

# check drift status
if horizontalOffset == 0 or verticalOffset == 0:
    driftStatus = "Undefined"
    driftAngle = -99999
elif driftAngle < 10:
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

# input for initial and final signal strength
initialSignalStrength = float(input("Enter the initial signal strength (in dB): "))
finalSignalStrength = float(input("Enter the final signal strength (in dB): "))

# calculate signal degradation
if finalSignalStrength == 0:
    signalDegradation = float(-999999)  # Avoid division by zero
    signalStatus = "Undefined"
else:
    signalDegradation = 10 * math.log10(initialSignalStrength / finalSignalStrength) 
    if -3 < signalDegradation < 0:
            signalStatus = "Minimal"
    elif -10 < signalDegradation <= -3:
        signalStatus = "Moderate"
    elif -10 <= signalDegradation < -20:
        signalStatus = "Severe"
    else:
        signalStatus = "Critical"

# ------------------ Part 5: Beacon Report ----------------------------
# TODO: Print beacon report
print("=" * 72)
print(f"{BEACON_ID} Beacon Report".center(72))
print("=" * 72)
print(f"Technician: {INTERN:>60}")
print(f"Employee ID: {INTERNID:>59}")
print("=" * 72)
print(f"Drift Angle: {driftAngle:>55.3f} deg")
print(f"Drift Status: {driftStatus:>58}")
print("=" * 72)
print(f"Signal Degradation: {signalDegradation:>49.4f} dB")
print(f"Signal Status: {signalStatus:>57}")
print("=" * 72)

# ------------------ Part 6: Closing Narrative ----------------------------
# TODO: Display 2-3 sentences wrapping up the lab story
print("Analysis complete. Beacon data has been logged and reported to the Service Technician.")
print("Orbitals and Galatic War Maps are coming back online and functioning within normal " \
"parameters.")
print(f"Good work, intern {INTERN}. You have successfully aided managed democracy.")
print("Victory was never in doubt.")
print("FOR SUPER EARTH!!!")
print("")
print("End of Report.")