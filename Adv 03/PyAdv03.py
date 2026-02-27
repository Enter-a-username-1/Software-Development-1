# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 03 
 ------------------------------------------------------
  Date: February 26, 2026
  
  Partners:
  Name 1:Kael Secrest
  Detailed Contributions: I wrote the main print statements of Part 1 and 3.
  I build the main loops in part 3 and the randomizer code.

  Name 2: William Rainey
  Detailed Contributions: I wrote the main print statements of Part 2 and 4 providing the story for the code. 
  I chose to continue the theme of the previous lab adventures. I also helped check and revise some/minor parts
  of part 3 to ensure that everything ran smoothly and nicely.
   
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Be sure to use comments and follow our coding standards.
        * Not too many comments but enough to explain what you are doing.
    3. Imports and Constants at the top
    4. Use descriptive variable names
    5. Display any calculations with units
    6. Do not let any lines (code or comments) go past 99 characters wife
    8. Rerun the code and test all possible outcomes
    9. DO NOT copy/paste from websites or GenAI.  Do your own work and understand your code
    10. Don't forget to add your names and contributions
       Include details of who did what and why, not just "partner 1 did part 1"

      
"""
# ------------------ Part 1: Imports and Constants ----------------------------
# Imports.  Only import libraries if you are going to use them
import math
import random

# Constants.  Make sure they are ALLCAPS
INTERNNAME = "John Helldiver"


# ------------------ Part 2: Introductory Narrative ----------------------------
# TODO: Display a short 3-5 sentence introduction
print(f"Hello {INTERNNAME}, the UGS needs your help.")
print("You are the only person avaliable at this moment")
print("You have been tasked with navigating the duct maze to fix a steam pipe " \
"leak on Melevon Creek.")
print("You have 200 seconds of oxygen to complete your task.  Good luck!")




# ------------------ Part 3: Ducting Maze ----------------------------
# TODO: Navigate the duct maze.  This is the bulk of the program
#       Must have at least one while and one for loop
#       Maze must be at least 6 intersections in the maze
#       Must have random encounters with steam pipe and maintenance bot
#Variables
Oxygen = 200
#Setting up variables to check for input
enteringInput1 = True
enteringInput2 = True
enteringInput3 = True
enteringInput4 = True
enteringInput5 = True
enteringInput6 = True
atIntersection1 = True
atIntersection2 = True
atIntersection3 = True
atIntersection4 = True
atIntersection5 = True
atIntersection6 = True
GameOver = False
#Random Path Generator
SLRinputChanger = random.randint(1, 10)
if SLRinputChanger <= 3:
  SLRinputChanger = "L"
  SLRinputChanger2 = "R"
elif SLRinputChanger <= 6:
  SLRinputChanger = "R"
  SLRinputChanger2 = "L"
else:
  SLRinputChanger = "S"
  SLRinputChanger2 = "L"

#Loops
GameOver = False
#first intersection
print(f"You have {Oxygen} seconds of oxygen remaining.")
print("You have reached the first intersection. Do you go Left, Right, or Straight?")
while atIntersection1 == True and GameOver == False:
  input1 = ""
  enteringInput1 = True
  while enteringInput1 == True:
    input1 = input("Enter L, R, or S: ").upper()
    if input1 in ["L", "R", "S"]:
      enteringInput1 = False
    else:
      print("Invalid input. Please enter L, R, or S.")
  if Oxygen <= 0:
    print("You have run out of oxygen! You lose the game.")
    GameOver = True
    break
  elif input1 == SLRinputChanger:
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == SLRinputChanger2:
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the first intersection without any encounters.")
    atIntersection1 = False

#second intersection
while atIntersection2 == True and GameOver == False:
  print(f"You have {Oxygen} seconds of oxygen remaining.")
  print("You have reached the second intersection. Do you go Left, Right, or Straight?")
  input2 = ""
  enteringInput2 = True
  while enteringInput2 == True:
    input2 = input("Enter L, R, or S: ").upper()
    if input2 in ["L", "R", "S"]:
      enteringInput2 = False
    else:
      print("Invalid input. Please enter L, R, or S.")
  if Oxygen <= 0:
    print("You have run out of oxygen! You lose the game.")
    GameOver = True
    break
  elif input2 == SLRinputChanger:
    print("You have encountered an oxygen tank! You gain 36 seconds of oxygen.")
    Oxygen += 36
  elif input2 == SLRinputChanger2:
    print("You have encountered an  Automaton! You lose 42 seconds of oxygen.")
    Oxygen -= 42
  else:
    print("You have successfully navigated the second intersection without any encounters.")
    atIntersection2 = False

#third intersection
while atIntersection3 == True and GameOver == False:
  print(f"You have {Oxygen} seconds of oxygen remaining.")
  print("You have reached the third intersection. Do you go Left, Right, or Straight?")
  input3 = ""
  enteringInput3 = True
  while enteringInput3 == True:
    input3 = input("Enter L, R, or S: ").upper()
    if input3 in ["L", "R", "S"]:
      enteringInput3 = False
    else:
      print("Invalid input. Please enter L, R, or S.")
  if Oxygen <= 0:
    print("You have run out of oxygen! You lose the game.")
    GameOver = True
    break
  elif input3 == SLRinputChanger:
    print("You have encountered a broken door! You lose 21 seconds of oxygen.")
    Oxygen -= 21
  elif input3 == SLRinputChanger2:
    print("You have successfully navigated the third intersection without any encounters.")
    atIntersection3 = False
  else:
    print("You have encountered a maintenance bot! You gain 19 seconds of oxygen.")
    Oxygen += 19

#fourth intersection
while atIntersection4 == True and GameOver == False:
  print(f"You have {Oxygen} seconds of oxygen remaining.")
  print("You have reached the fourth intersection. Do you go Left, Right, or Straight?")
  input4 = ""
  enteringInput4 = True
  while enteringInput4 == True:
    input4 = input("Enter L, R, or S: ").upper()
    if input4 in ["L", "R", "S"]:
      enteringInput4 = False
    else:
      print("Invalid input. Please enter L, R, or S.")
  if Oxygen <= 0:
    print("You have run out of oxygen! You lose the game.")
    GameOver = True
    break
  elif input4 == SLRinputChanger:
    print("You have successfully navigated the fourth intersection without any encounters.")
    atIntersection4 = False
  elif input4 == SLRinputChanger2:
    print("You have encountered a maintenance bot! You gain 20 seconds of oxygen.")
    Oxygen += 20
  else:
    print("You have encountered a busted tank! You lose 44 seconds of oxygen.")
    Oxygen -= 44

#fifth intersection
while atIntersection5 == True and GameOver == False:
  print(f"You have {Oxygen} seconds of oxygen remaining.")
  print("You have reached the fifth intersection. Do you go Left, Right, or Straight?")
  input5 = ""
  enteringInput5 = True
  while enteringInput5 == True:
    input5 = input("Enter L, R, or S: ").upper()
    if input5 in ["L", "R", "S"]:
      enteringInput5 = False
    else:
      print("Invalid input. Please enter L, R, or S.")
  if Oxygen <= 0:
    print("You have run out of oxygen! You lose the game.")
    GameOver = True
    break
  elif input5 == SLRinputChanger:
    print("You have successfully navigated the fifth intersection without any encounters.")
    atIntersection5 = False
  elif input5 == SLRinputChanger2:
    print("You have encountered a steam pipe leak! You lose 37 seconds of oxygen.")
    Oxygen -= 37
  else:
    print("You have encountered an oxygen tank! You gain 45 seconds of oxygen.")
    Oxygen += 45

#sixth intersection

while atIntersection6 == True and GameOver == False:
  print(f"You have {Oxygen} seconds of oxygen remaining.")
  print("You have reached the sixth intersection. Do you go Left, Right, or Straight?")
  input6 = ""
  enteringInput6 = True
  while enteringInput6 == True:
    input6 = input("Enter L, R, or S: ").upper()
    if input6 in ["L", "R", "S"]:
      enteringInput6 = False
    else:
      print("Invalid input. Please enter L, R, or S.")
  if Oxygen <= 0:
    print("You have run out of oxygen! You lose the game.")
    GameOver = True
    break
  elif input6 == SLRinputChanger:
    print("You have encountered an Automaton! You lose 60 seconds of oxygen.")
    Oxygen -= 60
  elif input6 == SLRinputChanger2:
    print("You have encountered a maintenance bot! You gain 52 seconds of oxygen.")
    Oxygen += 52
  else:
    print("You have successfully navigated the sixth intersection without any encounters.")
    atIntersection6 = False

# ------------------ Part 4: Closing Narrative ----------------------------
# TODO: Display one ending if you successfully navigate the maze
#       Display another if you run out of oxygen

if GameOver == False:
  print("You have successfully navigated the maze and fixed the steam pipe leak!")
  print(f"You had {Oxygen} seconds of oxygen remaining.")
  print("You have successfully aided managed democracy.")
  print("Good job intern! You have earned a promotion to Helldiver!")
  print(f"Congratulations {INTERNNAME}!")
else:
  print("You have failed to navigate the maze and fix the steam pipe leak.")
  print("You had no oxygen remaining.")
  print("You have failed managed democracy.")