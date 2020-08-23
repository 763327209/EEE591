#####################################################
# HW 1 Part 1 
# EEE 591: Python for Engineer
#
# ********************
# This program calculates the time it takes for a object to hit the ground
#####################################################
import math
G_CONSTANT = 9.81 # Gravity constant (g = 9.81 m/s^2)

h_temp =int ( input ("enter height: ")) 

if (10 <= h_temp <= 1000): 
    h = h_temp 
        
    init_v_temp = int( input ("enter initial upward velocity: ")) 
    
    if (-20 <= init_v_temp <= 20): 
        init_v = init_v_temp 

        if (init_v > 0): #if initial velocity is positive, calculate the new maximum height
            newHeight = init_v ** 2 / (2 * G_CONSTANT) # Calculate new maximum height = initial velociy ^2 / (2 * 9.81m/s^2)
            t_newHeight = init_v / G_CONSTANT # Calculate the time that takes the ball get to the new height
            updated_height = newHeight + h
            t_freeFall= math.sqrt((2 * updated_height)/ G_CONSTANT) # Free fall time (Downwards) = square root of ( 2 * height of the ball )/ (9.81 m/s^2)
            t_final = t_newHeight + t_freeFall # Total time = Time for Upwards (if the initial velocity is positive) + Time for Free fall
            
            print ('time to hit ground %.2f seconds' % t_final)
        
        elif (init_v <= 0): #if initial velocity is negative, count as free fall motion
            newHeight = init_v ** 2 / (2 * G_CONSTANT) 
            t_newHeight = init_v / G_CONSTANT 
            updated_height = newHeight + h
            t_freeFall= math.sqrt((2 * updated_height)/ G_CONSTANT) 
            t_final = t_newHeight + t_freeFall 
            
            print ('time to hit ground %.2f seconds' % t_final)
    
    else:
        print("Initial velocity is too large! Slow down!")
        quit

else: 
    print("Bad height specified. Please try again.") 
    quit