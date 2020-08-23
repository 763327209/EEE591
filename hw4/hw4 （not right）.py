##################################
# HW 4
# EEE 591: Python for Engineer
#Comments
#The output graph should print the analyses for 10 iterations and for a period of 70 years and not for 90 years.
##################################

import tkinter                           # we need to use tkinter for creating window
from tkinter import *                    # tired of typing tk?
import random                            # we need to use this to generate random number
import matplotlib                        # we need to use this to plot the graph
matplotlib.use("TkAgg")                  # need this BETWEEN import of matplotlib and pyplot!
import matplotlib.pyplot as plt          # importing pyplot! save key strokes


# function to get the values from the fields and clear the fields for the next entry
def show_entry_fields(e1,e2,e3,e4,e5,e6):
    
    mean = float(e1.get())                       #getting the mean value from the user input
    std = float(e2.get())                        #getting the standard deviation for the market value from the user input
    contribution = float(e3.get())               #getting the contribution value from the user input
    no_contribute = int(e4.get())                #getting the number of contribute years value from the user input
    no_retire = int(e5.get())                    #getting the number of retirement years value from the user input
    withdrawl = float(e6.get())                  #getting the yearly withdrawl after retire value from the user input
    
    #print("Mean Return (%%)  : %s\n"  %mean)                           #DEBUG PRINT
    #print("Std Dev Return (%%) : %s\n"  %std)                          #DEBUG PRINT
    #print("Yearly Contribution ($): %s\n"  %contribution)              #DEBUG PRINT
    #print("No. of Years of Contribution: %s\n"  %no_contribute)        #DEBUG PRINT
    #print("No. of Years to Retirement : %s\n"  %no_retire)             #DEBUG PRINT
    #print("Annual Spend in Retirement : %s\n"  %withdrawl)             #DEBUG PRINT


    
    balance_list = []    #create a list to gather the balance info
    
    balance_list.append (0) # append the year 0
    working = 0             # flag for identify whether this is the first year or not
    
    #now we are calculating the first portion: years that we need to working hard
    for index in range (0,int(no_contribute)):
        
        
        rand = random.uniform(-1, 1)    # generate a UNIF random number between -1 and 1
        rate = 1.0 +  (((mean/100.0) + (std*rand)/100.0 )) # now calculate this year's rate
         
        working = balance_list[index]   #now read and see whether this is the 0 year
        
        # if this is the 0th year, we only cumulate the contribution value plus the current market rate
        if (working == 0):
            working = contribution * rate  #cumulate the contribution value plus the current market rate
        
        # else, we read the balance from previous year, and then times the current market rate, and plus the yearly contribution
        else:

            working = (balance_list[-1] * rate) + contribution 
            
        balance_list.append (working)    # calculated result will be append to the balance list!
        
        #print (working)                 #DEBUG PRINT
        
    #print(balance_list)                 #DEBUG PRINT
    
    
    # now we aare calulating the portion where we are retired
    for index in range (0,int(no_retire)):
        
        
        rand = random.uniform(-1, 1)                        # generate a UNIF random number between -1 and 1
        rate = 1.0 +  (((mean/100.0) + (std*rand)/100.0 ))  # now calculate this year's rate
        retire = (balance_list[-1] * rate) - withdrawl      # we read the balance from previous year, and then times the current market rate, and subtract the yearly withdrawl since we are not working
        balance_list.append (retire)                        # calculated result will be append to the balance list!
        #print (retire)             #DEBUG PRINT
    #print(balance_list)            #DEBUG PRINT

    
    no_money_list = []                          #now we create a list for gathering info for running out of money.
    
    # now we need to test the balance list and see we are running out of money or not
    for index in range(0, len(balance_list)):   # read the index of the balance list from 0 to the length of the list
        test_positive = balance_list[index]     # get the n-th element from the list and test it!
        
        # if the balance is positive: we move on
        if (test_positive >= 0):
            continue
        
        # if the balance is negative, warning sign!!!!
        else:
            no_money_list.append (test_positive) # we need to append to the no money list for further investigation....
            balance_list[index] = 0              # this fix the nagtive balance to zero. Helps on graphing
            #print("index |%d| <0" % index,"value = %.2f" % test_positive)     #DEBUG PRINT
    
   #print(balance_list)                                                        #DEBUG PRINT
    total_sim_years = len(balance_list)        # get the total simulation year from the length of the balance list
    x_years = list(range(0,total_sim_years))   # now we are creating a list for the X-axis. Helps on graphing
    sim_year_report = total_sim_years -1       # report the total simulation year 
    #print("Total Simulation Years: %d" % sim_year_report)                     #DEBUG PRINT
    no_money_year = sim_year_report - len(no_money_list)   # the year that running out of money can be calculate.
    
    #If we haven't running out of money at desired simulation year, congrats!
    if (no_money_year == sim_year_report):
        #print("Yay! We still have $ %.2f" % balance_list[-1])                  #DEBUG PRINT
        
        # we now create a label and show the remaining balance on the window. 
        Label(master, text="Yay! We still have $ {:,}                                                  " .format(round(balance_list[-1],2)) ).grid(row=6,sticky = W)
    
    #If the year that money is running out is before the desired simulation year, oh no!
    else:
        #print("Running out of money at year: %d" % no_money_year)             #DEBUG PRINT
        
        # we now create a label and show the year that running our of money on the window. 
        Label(master, text="Oh no! We are running out of money at year: %d               " % no_money_year ).grid(row=6,sticky = W)
    
    
    
    
    plt.plot(x_years, balance_list)                   # plot the x-axis as the x_years, and thhe y axis as the balance_list
    plt.title('Account Balance Running Total for {} Years'.format(sim_year_report))    # title of the graph
    plt.xlabel("Number of Years")                     # x-axis
    plt.ylabel("Balance")                             # y-axis
    plt.show()                                        # show the plot
    pass #pass to tk
    
master = Tk()         
'Mean Return (%)', 'Std Dev Return (%)', 'Yearly Contribution ($)', \
          'No. of Years of Contribution ', 'No. of Years to Retirement', 'Annual Spend in Retirement'                          # top-level widget
Label(master,text="Mean Return (%)").grid(row=0)     # Labels - row says how to line then up
Label(master,text="Std Dev Return (%)").grid(row=1)
Label(master,text="Yearly Contribution ($)").grid(row=2)     # Labels - row says how to line then up
Label(master,text="No. of Years of Contribution").grid(row=3)
Label(master,text="No. of Years to Retirement").grid(row=4)     # Labels - row says how to line then up
Label(master,text="Annual Spend in Retirement").grid(row=5)



e1 = Entry(master)                              # mean value entry
e2 = Entry(master)                              # standard deviation for the market entry
e3 = Entry(master)                              # contribution value entry
e4 = Entry(master)                              # number of contribute years entry
e5 = Entry(master)                              # number of retirement years entry
e6 = Entry(master)                              # yearly withdrawl after retire entry

e1.grid(row=0,column=1)                         # mean value line up with their labels
e2.grid(row=1,column=1)                         # standard deviation for the market line up with their labels
e3.grid(row=2,column=1)                         # contribution value line up with their labels
e4.grid(row=3,column=1)                         # number of contribute years line up with their labels
e5.grid(row=4,column=1)                         # number of retirement years line up with their labels
e6.grid(row=5,column=1)                         # yearly withdrawl after retire line up with their labels


# add a button executes the command "master.destroy" when it is pressed, and has text "Quit"

Button(master,text='Quit',command=master.destroy).grid(row=7,column=0,sticky=W,pady=4)

# add a button executes the user-defined function: Calculate when it is pressed.

Button(master,text='Calculate',command=lambda: show_entry_fields(e1,e2,e3,e4,e5,e6)).grid(row=7,column=1,sticky=W,pady=4)

mainloop()     



