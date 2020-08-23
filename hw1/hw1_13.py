#################################################################################################################
# HW 1 Part 3 
# EEE 591: Python for Engineer
# 
# ********************
# This program calculates factorial, Catalan number, and the greatest common divisor of two nonnegative integers
#################################################################################################################

def factorial (fn): # Input of the function: fn
    if fn == 1: # Case 1 where factorial of 1 equals to 1
        return 1
    else: 
        last_num = fn-1 # Get the last input number
        return fn * factorial(last_num) #recursion
     
def catalan (cn): # Input of the function: fn
    if cn == 0: # Case 1 where Catalan of 1 equals to 1
        return 1
    else:
        last_num = cn - 1 # Get the last input number
        return (((4 * cn)-2)/(cn + 1)) * catalan(last_num) #recursion
       
def euclid (em,en): # Input of the function: em and en (Two numbers)
    if en == 0: # Case 1 where the en input equals to 0
        return em # Since one of the number is 0, the greatest common number will equals to the other one
    else:
        return euclid(en, (em % en)) # Case 2 where en input is not 0. Calculate their greatest common divisor    

fn = int(input ("Enter an integer for a factorial computation: ") )   
cn = int(input ("Enter an integer for a Catalan number computation: "))  
em = int(input ("Enter the first of two integers for a GCD calculation: "))  
en = int(input ("Enter the second integer for the GCD calculation: "))  

# Format the f_cal as integer 
f_cal = int(factorial(fn)) 

# Format the c_cal as a float 
c_cal = float(catalan (cn)) 

e_cal = euclid(em,en) 
    
print("") # carriage return
print('factorial of', fn,'is',f_cal) 
print('catalan value of', cn,'is',c_cal) 
print('greatest common divisor of',em,'and',en,'is',e_cal) 