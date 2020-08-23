#####################################################################################
# HW 2 Part 2
# EEE 591: Python for Engineer
# 
# This program calculate the Stefan-Boltzman from Planck theory of thermal radiation
#####################################################################################

import numpy as np                            # import required math functions
from scipy.integrate import quad              # quadrature integration
import math                                   # required for round_sigfig function

# Constants for the program                          
HBAR = 1.055e-34                            # Planck's constant over 2 Pi
BOLTZ = 1.381e-23                           # Blotzmann's constant
C = 2.998e8                           # speed of light

# Utility function to control the significant numbers

def round_sigfig(num, sig_fig):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_fig - 1)))
    else:
        return 0  # Can't take the log of 0
    
# function to calculate the total energy per unit area radiated by a black body

def W_integral (x):
    W_1st = (BOLTZ ** 4) / (4 * (np.pi ** 2) * (C ** 2) * (HBAR **3)) # first part of the function
    expression = (W_1st) * (x **3)/(-1 + np.exp(x))                            # final expression for the function
    return expression

integral_result , err = quad (W_integral, 0, np.inf)        # doing integration from 0 to infinity

rounded = round_sigfig(integral_result,4)                   # rounding the integration result to 4 sigfigs

print('The Stefan-Boltzman constant is',rounded,'.')        
