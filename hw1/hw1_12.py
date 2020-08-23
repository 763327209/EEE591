#####################################################
# HW 1 Part 2 
# EEE 591: Python for Engineer
# 
# ********************
# This program finds the prime number from 3 to 10000
#####################################################

import math

my_prime = [] # Create a list for storing prime numbers
my_prime.append(2) # Append the first prime number into the list

index = 0 # Initialize the index number for the list as 0

for num in range (3,10001):
    num_sqrt = (math.sqrt(num)) #calculating the square root of the num
    is_prime = True 
    
    for index in range(0,len(my_prime),1) : # index range from 0 to length of the prime number list with increment by 1
        stored = my_prime[index] # Getting the (index) of element, and pass it to variable "stored"
        if (stored > num_sqrt): 
            break 
        if (num % stored == 0): # If the generated number is divisible, it's NOT a prime number
            is_prime = False 
            break
    if (is_prime == True): # If the is_prime variable is still True, this is a prime number
        my_prime.append(num) 

print (my_prime) 