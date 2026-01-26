# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 01 
 ----------------------------
  Date: 1 / 13 / 2026
  Partner 1 Name: Kael Secrest
  Partner 1 Contributions: Code parts 1-4

  Partner 2 Name: 
  Partner 2 Contributions: Story, code part 5
   
      
      
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
UseName = ""
IDNum = ""
SectorNum = ""
PlanetName = ""

# ------------------ Part 1: Introduction ----------------------------
# TODO: Display a short narrative introducing the situation
# Make it 3-5 sentences
print("Welcome to Galactic HR Systems!")
print("You have been hired as a new employee in the Galactic Federation.") 



# ------------------ Part 2: HR System  ----------------------------
# TODO: prompt the user for name, tempID, sector number and planet
UseName = input("Enter your name: ")
TempIDNum = str(input("Enter your temporary ID: "))
SectorNum = input("Enter your sector number: ")
PlanetName = input("Enter your planet name: ")



# ------------------ Part 3: Create Employee ID and calculate pay rates  ----------------------------
# TODO: convert 4 digit temporary ID to 11 digit employee ID
# TODO: Calculate pay rates for day, weekend, overtime, subspace and hyperspace
BackID = TempIDNum[3] + TempIDNum[2] + TempIDNum[1] + TempIDNum[0]
IDNum = SectorNum + TempIDNum + SectorNum + str(BackID)
CheckSum = int(IDNum[0]) + int(IDNum[1]) + int(IDNum[2]) + int(IDNum[3]) + int(IDNum[4]) + int(IDNum[5]) + int(IDNum[6]) + int(IDNum[7]) + int(IDNum[8]) + int(IDNum[9]) + int(IDNum[10])

# ------------------ Part 4: Output Employee HR Report ----------------------------
# TODO: output an HR report with employee information and payrates
# make sure all columns line up
print("Employee ID:", IDNum)
print("Name:", UseName)
print("Sector Number:", SectorNum)
print("Planet Name:", PlanetName)
print("CheckSum:", CheckSum)

# ------------------ Part 5: Closing  ----------------------------
# TODO: Display 2-3 sentences wrapping up the lab story

