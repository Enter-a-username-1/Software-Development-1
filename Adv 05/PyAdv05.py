# -*- coding: utf-8 -*-
"""
 
  Program: CSC115 Lab Adventure 05
 ------------------------------------------------------
  Date: April 9, 2026
 
  Partners:
  Name 1: Kael Secrest
  Detailed Contributions:
      
 
  Name 2: William Rainey
  Detailed Contributions:
      I wrote the main narrative text and helped with the formatting of the output.
      I also helped test the main code to ensure there were no bugs.
 
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
    ---- PROVIDED BY PROFESSOR - DO NOT MODIFY ----
    This function reads a data file into a 1D NumPy array of ints.
 
    Parameter:
        filename (str): path/name of the file to read
 
    Return:
        nd array of ints, or None if an error occurs
 
    Example:
        myarray = read_numpy_data('mydata.raw')
    """
    import os
 
    # Change directory to same location as the program save location
    try:
        # Works for .py files
        os.chdir(os.path.dirname(__file__))
 
    except Exception as e:
        # If error, try Jupyter notebook method
        print(f"   Error: {e}.  Trying Jupyter notebook method")
        os.chdir(os.path.dirname(globals()["__vsc_ipynb_file__"]))
 
    # Load data from filename into numpy array
    try:
        array = np.loadtxt(filename, dtype='int')
        print(f"{filename} successfully read into NumPy array")
    except Exception as e:
        print("Error:", e)
        return None
    else:
        return array
 
 
# ------------------ Part 2B: plot_signals function ----------------------------
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
    # Build an array of sector numbers for the x-axis
    sectors = np.arange(NUM_SECTORS)
 
    # Create the figure and plot each rate as a separate line
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
# 5-sentence Helldivers-themed opening
 
print(f"""
{'=' * 80}
   SUPER EARTH HELLDIVER INTELLIGENCE DIVISION -- CLASSIFIED BRIEFING
{'=' * 80}
 
Helldiver {INTERNNAME}, your boots are barely dry from the last op on Tibit,
but Super Earth needs you again this time the mission is data, not bullets.
 
Our signals analysts have intercepted millions of HIL beacon IDs flooding in
from every sector of the galaxy, and something is very wrong with the numbers.
 
The automaton sympathizer known only as Lyra has been flooding the network with
spoofed IDs, but one sector is suspiciously quiet -- and silence on the
battlefield always means someone is hiding.
 
Your Personal Hellpad has been loaded with the raw intercept files; all you
need to do is run the analysis and pinpoint the sector so we can drop in and
drag Lyra back to face Managed Democracy.
 
For Super Earth, Helldiver. Do not miss.
{'=' * 80}
""")
 
 
# ------------------ Part 3B: Call the Read Data Function ----------------------------
print("Downloading intercept data to Personal Hellpad...\n")

# --- Use test files first; swap to real files once results match ---
sector_data = read_numpy_data('test_sectordata.raw')   # change to 'sectordata.raw' for real data
status_data = read_numpy_data('test_statusdata.raw')   # change to 'statusdata.raw' for real data

# Stop here if either file failed to load
if sector_data is None or status_data is None:
    print()
    print("MISSION ABORT: Data files could not be loaded.")
    print("Make sure the .raw files are in the same folder as PyAdv05.py")
    quit()

print()
 
 
# ------------------ Part 3C: Calculate rates  ----------------------------
# Count total IDs per sector (0-9) using np.bincount
total_per_sector = np.bincount(sector_data, minlength=NUM_SECTORS)
 
# Count each status type per sector using np.bincount with a sector slice
invalid_per_sector = np.bincount(sector_data[status_data == INVALID_ID],
                                 minlength=NUM_SECTORS)
spoofed_per_sector = np.bincount(sector_data[status_data == SPOOFED_ID],
                                 minlength=NUM_SECTORS)
corrupt_per_sector = np.bincount(sector_data[status_data == CORRUPT_ID],
                                 minlength=NUM_SECTORS)
 
# Compute the rate (%) of each status type per sector
invalid_rate = 100 * (invalid_per_sector / total_per_sector)
spoof_rate   = 100 * (spoofed_per_sector / total_per_sector)
corrupt_rate = 100 * (corrupt_per_sector / total_per_sector)
 
 
# ------------------ Part 3D: Plot all 3 rates ----------------------
# Call the plotting function with the three computed rate arrays
plot_signals(spoof_rate, invalid_rate, corrupt_rate)
 
 
# ------------------ Part 3E: Display statistics ----------------------
# Compute overall totals for display
total_ids   = len(sector_data)
total_inv   = np.sum(status_data == INVALID_ID)
total_spoof = np.sum(status_data == SPOOFED_ID)
total_corr  = np.sum(status_data == CORRUPT_ID)
 
# Compute spoof rate statistics
spoof_mean       = np.mean(spoof_rate)
spoof_std        = np.std(spoof_rate)
spoof_min        = np.min(spoof_rate)
spoof_max        = np.max(spoof_rate)
spoof_min_sector = np.argmin(spoof_rate)
spoof_max_sector = np.argmax(spoof_rate)
 
# Round the spoof rate array to 2 decimals for cleaner display
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
# Check if the minimum spoof rate matches the known correct value and display
# the appropriate Helldivers-themed ending
 
if round(spoof_min, 8) == CORRECT_MIN:
    # --- Correct result: real data was used ---
    print(f"""
        [The graph stabilizes. One sector flatlines far below the rest.]
 
        {INTERNNAME}: Sector {spoof_min_sector} has the lowest spoof rate, sir.
 
        Command: ...There you are, Lyra.
 
            She is hiding in Sector {spoof_min_sector}. Grab your Hellpod.
            We are going on a trip.
 
        You slam the beacon coordinates into your Stratagem terminal and
        sprint to the drop bay. The Pelican's engines scream to life as
        the nav-computer locks on Sector {spoof_min_sector}.
 
        Lyra does not know it yet -- but the next thing she will hear
        is the sound of a Hellpod punching through her roof.
 
        FOR SUPER EARTH.
    """)
 
else:
    # --- Incorrect result: still using test data or math error ---
    print(f"""
        Command: Stand down, {INTERNNAME}. Your numbers are wrong.
 
        Are you sure that is the correct lowest spoofed ID rate?
        I thought it was closer to {CORRECT_MIN}%
 
        Ah...you must still be using the test data.
 
        Try again and this time, use the real intercept files I gave you.
        Super Earth did not train you to guess -- get it right.
    """)