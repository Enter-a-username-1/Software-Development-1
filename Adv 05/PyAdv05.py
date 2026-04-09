# -*- coding: utf-8 -*-
"""
 
  Program: CSC115 Lab Adventure 05
 ------------------------------------------------------
  Date: April 9, 2026
 
  Partners:
  Name 1: Kael Secrest
  Detailed Contributions:
      Wrote the code to caulculate the rates of spoofed and output the results.
      I also wrote the function code.
      I also tested the code for bugs.
 
  Name 2: William Rainey
  Detailed Contributions:
      I wrote the main text for the story.
      I also wrote the code that reads the data from the file.
      I also helped test the code to ensure there were no bugs.
 
"""
 
###################################################################################################
# ------------------ Part 1: Imports and Constants ----------------------------
###################################################################################################
# Import numpy for array operations and matplotlib for plotting
 
import numpy as np
import matplotlib.pyplot as plt
 
# --- Constants ---
 
CORRECT_MIN = 3.60765074   # correct min spoof rate rounded to 8 decimals
 
VALID_ID   = 0   # status code for a valid ID
INVALID_ID = 1   # status code for an invalid ID
SPOOFED_ID = 2   # status code for a spoofed ID
CORRUPT_ID = 3   # status code for a corrupt ID
 
NUM_SECTORS = 10  # sectors are numbered 0-9
 
INTERNNAME = "John Helldiver"
 
 
###################################################################################################
# ------------------ Part 2: Function Definitions ----------------------------
###################################################################################################
def read_numpy_data(filename):
    """
    ---- PROVIDE BY PROFESSOR - DO NOT MODIFY ----
    This function reads data file into a 1D NumPy array of ints
    Parameter: 
        str -> filename
    Return:
        nd array of ints or None if an error occurs
    Example:
        myarray = read_numpy_data('mydata.raw')
    """
    import os

    # change directory to same as the program save location
    try:
        # works for py files
        os.chdir(os.path.dirname(__file__))
        
    except Exception as e:
        # if error, try Jupyter notebook method
        print(f"   Error: {e}.  Trying Jupyter notebook method")
        
        os.chdir(os.path.dirname(globals()["__vsc_ipynb_file__"]))

    # load data from filename into numpy array
    try:
        array = np.loadtxt(filename, dtype='int')
        print(f"{filename} successfully read into NumPy array")
    except Exception as e:
        print("Error:", e)
        return None
    else:
        return array
 
 
# ------------------ Part 2B: plot_signals function ----------------------------
# TODO: write function to plot spoof_rate, invalid_rate, corrupt_rate
# besure to include title, x/y labels, legend, grid 
def plot_signals(spoof_rate, invalid_rate, corrupt_rate):
    """
    Plots the spoofed, invalid, and corrupt ID rates across all sectors
    using matplotlib.
 
    Parameters:
        spoof_rate  (ndarray): percentage of spoofed IDs per sector
        invalid_rate(ndarray): percentage of invalid IDs per sector
        corrupt_rate(ndarray): percentage of corrupt IDs per sector
 
    Return:
        None (void function)
 
    Example:
        plot_signals(spoof_rate, invalid_rate, corrupt_rate)
    """

    sectors = np.arange(NUM_SECTORS)
 
    plt.figure(figsize=(10, 6))
 
    plt.plot(sectors, spoof_rate,   marker='o', label='Spoof Rate (%)',   color='crimson')
    plt.plot(sectors, invalid_rate, marker='s', label='Invalid Rate (%)', color='darkorange')
    plt.plot(sectors, corrupt_rate, marker='^', label='Corrupt Rate (%)', color='steelblue')
 
    # Labels, title, legend, and grid
    plt.title('HIL Network ID Anomaly Rates by Sector', fontsize=14, fontweight='bold')
    plt.xlabel('Sector Number', fontsize=12)
    plt.ylabel('Rate (%)', fontsize=12)
    plt.xticks(sectors)
    plt.legend()
    plt.grid(True)
 
    plt.tight_layout()
    plt.show()
 
 
###################################################################################################
# ------------------ Part 3: Main Code ----------------------------
###################################################################################################
 
# ------------------ Part 3A: Opening Narrative ----------------------------
# TODO: simple 5 sentence opening
 
print(f"""
{'=' * 80}
   SUPER EARTH HELLDIVER DIVISION BRIEFING
{'=' * 80}
 
Dear Helldiver {INTERNNAME}, thanks for your help back on Tibit,
However, Super Earth needs you to crunch data.
The GIS have intercepted millions of HIL beacon IDs flooding in
from every sector of the galaxy, and something is very wrong with all the numbers.
The automaton sympathizer known only as Lyra has been flooding the network with
spoofed IDs, but one sector is suspiciously quiet and silence on the
battlefield always means someone is hiding.
Your Hellpad has been loaded with the raw intercept files; all you
need to do is run the analysis and find the sector so we can drop in and
find whoever Lyra is so they can face Managed Democracy.
 
For Super Earth.
{'=' * 80}
""")
 
 
# ------------------ Part 3B: Call the Read Data Function ----------------------------
# TODO: Read sector and status data from raw files using provided read_numpy_data function
print("Downloading data to Hellpad...\n")

sector_data = read_numpy_data('sectordata.raw')
status_data = read_numpy_data('statusdata.raw')

# If either file failed to load
if sector_data is None or status_data is None:
    print()
    print("MISSION ABORT: Data files could not be loaded. We have failed Super Earth.")
    quit()

print()
 
 
# ------------------ Part 3C: Calculate rates  ----------------------------
# TODO: Count total IDs per sector (0–9) using np.bincount
# Count spoofed, invalid and corrupt IDs per sector using np.bincount
# Compute spoofed, invalid, corrupt rate per sector as a percentage ie: spoofrate = spoofid / total

total_per_sector = np.bincount(sector_data, minlength=NUM_SECTORS)

invalid_per_sector = np.bincount(sector_data[status_data == INVALID_ID], minlength=NUM_SECTORS)
spoofed_per_sector = np.bincount(sector_data[status_data == SPOOFED_ID], minlength=NUM_SECTORS)
corrupt_per_sector = np.bincount(sector_data[status_data == CORRUPT_ID], minlength=NUM_SECTORS)
 
# Figure the percent of each status type per sector
invalid_rate = 100 * (invalid_per_sector / total_per_sector)
spoof_rate   = 100 * (spoofed_per_sector / total_per_sector)
corrupt_rate = 100 * (corrupt_per_sector / total_per_sector)
 
 
# ------------------ Part 3D: Plot all 3 rates ----------------------
# TODO: call the function to plot spoofed rate, invalid rate, corrupt rate
plot_signals(spoof_rate, invalid_rate, corrupt_rate)
 
 
# ------------------ Part 3E: Display statistics ----------------------
# TODO: display the IDs analyzed and number of spoofed, invalid and corrupt ids
# display the mean, standard deviation, min, min location, max and max location of the spoofed ids
total_ids   = len(sector_data)
total_inv   = np.sum(status_data == INVALID_ID)
total_spoof = np.sum(status_data == SPOOFED_ID)
total_corr  = np.sum(status_data == CORRUPT_ID)
 
# Compute spoof rate stats
spoof_mean       = np.mean(spoof_rate)
spoof_std        = np.std(spoof_rate)
spoof_min        = np.min(spoof_rate)
spoof_max        = np.max(spoof_rate)
spoof_min_sector = np.argmin(spoof_rate)
spoof_max_sector = np.argmax(spoof_rate)
 
# Round the spoof rate
spoof_display = np.round(spoof_rate, 2)
 
# Display the results table
print(f"   Results:")
print(f"   -------------")
print(f"   IDs Analyzed: {total_ids:,}")
print(f"   Invalid IDs:  {total_inv:,}")
print(f"   Spoofed IDs:  {total_spoof:,}")
print(f"   Corrupt IDs:  {total_corr:,}")
print()
print(f"   Spoof Rate:")
print(f"   ----------------")
print(f"   by sector: {spoof_display}")
print(f"   mean:      {spoof_mean:.2f}%")
print(f"   std dev:   {spoof_std:.2f}%")
print(f"   min:       {spoof_min:.2f}% in sector {spoof_min_sector}")
print(f"   max:       {spoof_max:.2f}% in sector {spoof_max_sector}")
print()
 
 
# ------------------ Part 3F: Closing Narrative ----------------------------
# TODO: check to see if the min spoof rate value is correct and display the
# appropriate simple 2-3 sentence closing
 
if round(spoof_min, 8) == CORRECT_MIN:
    #Gets a correct result
    print(f"""
        Sector {spoof_min_sector} has the lowest spoof rate.
        That must be Lyra.
        She is hiding in Sector {spoof_min_sector}. Get in your ship
        You are going to sector {spoof_min_sector} to find her and end this.
        Good luck, {INTERNNAME}. You are going to need to beat her.
        It is necissary in order to change the tide of the war with the automatons.
 
        For Super Earth.
    """)
 
else:
    #Doesnt get a correct result
    print(f"""
        {INTERNNAME} Your numbers seem off.
        Are you sure that is the correct lowest spoofed ID rate
        It was supposed to be closer to {CORRECT_MIN}%
        Try again and this time, use different data that just came in.
        We don't make wrong guesses in Managed Democracy.
        For Super Earth.
    """)