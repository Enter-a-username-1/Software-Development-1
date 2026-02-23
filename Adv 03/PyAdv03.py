# -*- coding: utf-8 -*-
"""

  Program: CSC115 Lab Adventure 03 
 ------------------------------------------------------
  Date:
  
  Partners:
  Name 1:Kael Secrest
  Detailed Contributions:   

  Name 2:
  Detailed Contributions: 
   
      
      
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


# Constants.  Make sure they are ALLCAPS
INTERNNAME = "John Helldiver"




# ------------------ Part 2: Introductory Narrative ----------------------------
# TODO: Display a short 3-5 sentence introduction
print(f"Hello {INTERNNAME}, the UGS needs your help.")
print("You have been tasked with navigating the duct maze to fix a steam pipe " \
"leak on Melevon Creek.")
print("You have 300 seconds of oxygen to complete your task.  Good luck!")







# ------------------ Part 3: Ducting Maze ----------------------------
# TODO: Navigate the duct maze.  This is the bulk of the program
#       Must have at least one while and one for loop
#       Maze must be at least 6 intersections in the maze
#       Must have random encounters with steam pipe and maintenance bot
#Variables
Oxygen = 300


#Loops
while True:
  #first intersection
  print("You have reached the first intersection. Do you go Left, Right, or Straight?")
  while True:
    input1 = input("Enter L, R, or S: ")
    if input1 in ["L", "R", "S"]:
        break
    print("Invalid input. Please enter L, R, or S.")
  if input1 == "L":
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == "R":
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the first intersection without any encounters.")

  #second intersection
  print("You have reached the second intersection. Do you go Left, Right, or Straight?")
  while True:
    input1 = input("Enter L, R, or S: ")
    if input1 in ["L", "R", "S"]:
        break
    print("Invalid input. Please enter L, R, or S.")
  if input1 == "L":
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == "R":
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the second intersection without any encounters.")

  #third intersection
  print("You have reached the third intersection. Do you go Left, Right, or Straight?")
  while True:
    input1 = input("Enter L, R, or S: ")
    if input1 in ["L", "R", "S"]:
        break
    print("Invalid input. Please enter L, R, or S.")
  if input1 == "L":
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == "R":
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the first intersection without any encounters.")

  #fourth intersection
  print("You have reached the second intersection. Do you go Left, Right, or Straight?")
  while True:
    input1 = input("Enter L, R, or S: ")
    if input1 in ["L", "R", "S"]:
        break
    print("Invalid input. Please enter L, R, or S.")
  if input1 == "L":
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == "R":
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the first intersection without any encounters.")

  #fifth intersection
  print("You have reached the fifth intersection. Do you go Left, Right, or Straight?")
  while True:
    input1 = input("Enter L, R, or S: ")
    if input1 in ["L", "R", "S"]:
        break
    print("Invalid input. Please enter L, R, or S.")
  if input1 == "L":
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == "R":
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the first intersection without any encounters.")

  #sixth intersection
  print("You have reached the sixth intersection. Do you go Left, Right, or Straight?")
  while True:
    input1 = input("Enter L, R, or S: ")
    if input1 in ["L", "R", "S"]:
        break
    print("Invalid input. Please enter L, R, or S.")
  if input1 == "L":
    print("You have encountered a steam pipe leak! You lose 50 seconds of oxygen.")
    Oxygen -= 50
  elif input1 == "R":
    print("You have encountered a maintenance bot! You gain 30 seconds of oxygen.")
    Oxygen += 30
  else:
    print("You have successfully navigated the first intersection without any encounters.")









# ------------------ Part 4: Closing Narrative ----------------------------
# TODO: Display one ending if you successfully navigate the maze
#       Display another if you run out of oxygen


