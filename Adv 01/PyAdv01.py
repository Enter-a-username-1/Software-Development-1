# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 01 
 ----------------------------
  Date: 1 / 13 / 2026
  Partner 1 Name: Kael Secrest
  Partner 1 Contributions: Code parts 1-3

  Partner 2 Name: William Rainey
  Partner 2 Contributions: Story, code part 4-5
   
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Be sure to use comments and follow our coding standards.
        * Not too many comments but enough to explain what you are doing.
        * In this first lab I will provide some comments for you to follow
    3. Use descriptive variable names
    4. Display calculations with units
    5. Do not let any lines (code or comments) go past 99 characters wife
    6. Make sure your table output lines up
    7. Rerun the code and test the output with different input values before submitting
    8. DO NOT copy/paste from websites or GenAI.  Do your own work.
      
"""
# Put constants here.  Make sure the variables are ALLCAPS
# good constants are the company name, your university name, the AI name etc
import random
UseName = ""
IDNum = ""
SectorNum = ""
PlanetName = ""

#This will make a random rate between 15 and 30 credits an hour
PayRate = random.uniform(15, 30)
#PayRate = 30.0 # fixed pay rate if wanted
WeekendRate = PayRate * 1.223
OvertimeRate = PayRate * 1.4832
SubTravelRate = PayRate * 0.1167
HyperTravelRate = PayRate * 0.1833

# ------------------ Part 1: Introduction ----------------------------
# TODO: Display a short narrative introducing the situation
# Make it 3-5 sentences
print("Welcome to Galactic HR Systems!")
print("You have been hired as a new employee in the weapons department.")
print("You job is to helpcreate new weapons for the United States of the Galactic.")
print("To get started we need to create your employee ID and calculate your pay rates.") 
print("Your ship hanger is building 6 level 7.")

# ------------------ Part 2: HR System  ----------------------------
# TODO: prompt the user for name, tempID, sector number and planet
UseName = input("Enter your name: ")
TempIDNum = str(input("Enter your temporary ID: "))
SectorNum = input("Enter your sector number: ")
PlanetName = input("Enter your planet name: ")

# ------------------ Part 3: Create Employee ID and calculate pay rates  --------------------------
# TODO: convert 4 digit temporary ID to 11 digit employee ID
# TODO: Calculate pay rates for day, weekend, overtime, subspace and hyperspace
BackID = TempIDNum[3] + TempIDNum[2] + TempIDNum[1] + TempIDNum[0]
IDNum = SectorNum + TempIDNum + SectorNum + str(BackID)
CheckSum = int(IDNum[0]) + int(IDNum[1]) + int(IDNum[2]) + int(IDNum[3]) + int(IDNum[4]) + int(IDNum[5]) + int(IDNum[6]) + int(IDNum[7]) + int(IDNum[8]) + int(IDNum[9])
CheckSum = CheckSum % 10
IDNum = SectorNum + TempIDNum + SectorNum + str(BackID) + str(CheckSum)

# ------------------ Part 4: Output Employee HR Report ----------------------------
# TODO: output an HR report with employee information and payrates
# make sure all columns line up
print("")
print("HIL Q.U.A. Report".center(47))
print("=" * 47)
print(f"| {'Employee ID:':<16} {IDNum:>26} {'|':>1}")
print(f"| {'Name:':<16} {UseName:>26} {'|':>1}")
print(f"| {'Sector Number:':<16} {SectorNum:>26} {'|':>1}")
print(f"| {'Planet Name:':<16} {PlanetName:>26} {'|':>1}")
print(f"| {'CheckSum:':<16} {CheckSum:>26} {'|':>1}")
print("=" * 47)

print("Pay Rates".center(47))

print("=" * 47)
print(f"| {'Day Rate:':<16} {PayRate:>22.1f} {'Cr. |':>2}")
print(f"| {'Weekend Rate:':<16} {WeekendRate:>22.1f} {'Cr. |':>1}")
print(f"| {'Overtime Rate:':<16} {OvertimeRate:>22.1f} {'Cr. |':>1}")
print(f"| {'Sub Travel:':<16} {SubTravelRate:>22.1f} {'Cr. |':>1}")
print(f"| {'Hyper Travel:':<16} {HyperTravelRate:>22.1f} {'Cr. |':>1}")
print("=" * 47)

# ------------------ Part 5: Closing  ----------------------------
# TODO: Display 2-3 sentences wrapping up the lab story
print("Scary scenes are happening all around the universe, right now. Good thing You have made the most important decision of your life joining the GUS." )
print("You are now apart of an elite peace keeping force. You are helping spread managed democracy through the galaxy. You are now a hero, a legend. ")
print("Welcome to the team,", UseName + ".", "\n")
print("Now that you have your ID and pay rates, you're ready to start working on new weapons for the Galactic United States.")