#####################################################
# HW 2 Part 1
# EEE 591: Python for Engineer
#
# Exercise 5.10 Period of an anharmonic oscillator                           
#####################################################

import numpy as np                 # need PI, sqrt, arrays
from scipy.integrate import quad   # need to integrate
import matplotlib.pyplot as plt    # need to plot

PI = np.pi                         
MASS = 1                           

# Compute the potential at a point in the well                     

def V(x):                     # describes the potential distance x from center
    poten = x**8 + 3 * x**4        
    return poten

# Compute the function to be integrated a a specific spot          

def arg(z, pot):                        # pass the potential as an argument
    fin = 1 / np.sqrt( pot - V(z) )   
    return fin

amplitudes = np.arange(0.1,2,0.01)        # create the amplitudes for evaluation
num_amps = len(amplitudes)                # how many samples for evaluation
T = np.zeros(num_amps,float)      # array to hold the answers
for index in range(num_amps):             # loop through the amplitudes
    amp = amplitudes[index]                            
    potential =  V(amp)                             
    res,err = quad(arg,0.01,amp,args=(potential))   # integrate
    T[index] = res                             

T *= np.sqrt( 8.0 * MASS )    # use convenience of multiplying an array
plt.plot(amplitudes,T)        # plot the integrals versus the amplitude
plt.xlabel("amplitude")
plt.ylabel("period")
plt.show()
