##########################################################
# HW 3
# EEE 591: Python for Engineer
# 
# ********************
# Program to solve resister network with a voltage source
##########################################################

import numpy as np                     # needed for arrays
from numpy.linalg import solve         # needed for matrices
from read_netlist import read_netlist  # supplied function to read the netlist
import comp_constants as COMP          # needed for the common constants
import copy                            # needed for deep copying the list


# this is the list structure that we'll use to hold components:
# [ Type, Name, i, j, Value ] ; set up an index for each component's property

############################################################
# How large a matrix is needed for netlist? This could     #
# have been calculated at the same time as the netlist was #
# read in but we'll do it here to handle special cases     #                                       #
############################################################

def ranknetlist(netlist):              # pass in the netlist
    
    
    gather_begin = [item[2] for item in netlist]       # Gather Node i info from the netlist
    gather_end = [item[3] for item in netlist]         # Gather Node j info from the netlist
    gather_begin.pop(0)                                # Delete the first row of the Node i, which is the Node i for the Voltage or Current
    gather_end.pop(0)                                  # Delete the first row of the Node j, which is the Node j for the Voltage or Current
    
    #print(gather_begin)                               # DEBUG PRINT
    #print(gather_end)                                 # DEBUG PRINT
    
    nodes = zip(gather_begin,gather_end)               # map the similar index of Node i and Node j list
    nodes = set(nodes)                                 # converting values to print as set
    #print(nodes)                                      # DEBUG PRINT
    
    updated_begin = list(dict.fromkeys(gather_begin))  # Delete the duplicated nodes that inside Node i list
    updated_end = list(dict.fromkeys(gather_end))      # Delete the duplicated nodes that inside Node j list
    #print(updated_begin)                              # DEBUG PRINT
    #print(updated_end)                                # DEBUG PRINT
    
    counting_nodes = copy.deepcopy(updated_begin)      # deep copy everything from the Node i list to a new variable: counting_nodes
    counting_nodes.extend(updated_end)                 # place the elements that in Node j list to the end of the Node i list
    #print(counting_nodes)                             # DEBUG PRINT
    max_node = max(counting_nodes)                     # Get the maximum number from the list
    #print (max_node)                                  # DEBUG PRINT

    return max_node                                    # return the found maximum number of nodes

################################################################
# Function to stamp the components into the netlist            #
################################################################

def stamper(y_add,netlist,currents,num_nodes): # pass in the netlist and matrices

    flag = 0                                          # flag to identify whether it's a voltage or current source
    
    for comp in netlist:                              # for each component...
  
        # extract the i,j and fill in the matrix...
        # subtract 1 since node 0 is GND and it isn't included in the matrix

        if ( comp[COMP.TYPE] == COMP.R ):           # if the type is a resistor
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1
            if (i >= 0):                            # add on the diagonal: upper left
                y_add[i,i] += 1.0/comp[COMP.VAL]
                
            if (j >= 0):                            # add on the diagonal: lower right
                y_add[j,j] += 1.0/comp[COMP.VAL]
                
            if (j >= 0 and i >= 0):                 # add on the diagonal: upper right and lower left
                y_add[i,j] += - 1.0/comp[COMP.VAL]    
                y_add[j,i] += - 1.0/comp[COMP.VAL] 
        
        
        
        elif ( comp[COMP.TYPE] == COMP.VS ):        # if the type is a voltage source
            
            flag = 1                                # voltage source detected
            
            #add extra row and column [row,column]
            y_add = np.append(y_add, np.zeros([1, max_nodes]) ,axis = 0)       #add extra column to the most right resistor matrix (matrix A)
            y_add = np.append(y_add, np.zeros([max_nodes + 1, 1]) ,axis = 1)   #add extra row to the bottom of the resistor matrix (matrix A)
            
            currents = np.append(currents, np.zeros([1, 1]) ,axis = 0)         #add extra row to the bottom of the current matrix (matrix C)
            
            # extract the i,j and fill in the matrix...
            # subtract 1 since node 0 is GND and it isn't included in the matrix
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1
            #print(nodes)                          # DEBUG PRINT
            #print(currents)                       # DEBUG PRINT
            #print(y_add)                          # DEBUG PRINT
            
            if (i >= 0):                           # if node i (positive) is greater than 0
                y_add[i, max_nodes] +=  1.0        # set matrix A column [i, max_nodes] = 1
                y_add[max_nodes, i] +=  1.0        # set matrix A row [max_nodes, i] = 1
            if (j >= 0):
                y_add[j, max_nodes] += - 1.0       # set matrix A column [j, max_nodes] = -1
                y_add[max_nodes, j] += - 1.0       # set matrix A row [j, max_nodes] = -1

            currents[-1,0] += comp[COMP.VAL]       # finally, set the last row of the current (Matrix C) as the given voltage value
            
           
            
        elif ( comp[COMP.TYPE] == COMP.IS ):       # if the type is a current source
            
            # extract the i,j and fill in the matrix...
            # subtract 1 since node 0 is GND and it isn't included in the matrix
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1    
        
            if (i > j):                            # if node i (positive) is greater than node j
                currents[i] += - comp[COMP.VAL]    # set matrix C [i] = given current value
                
            elif (j > i):                          # if node j (negative) is greater than node i
                currents[j] +=  comp[COMP.VAL]     # set matrix C [j] = given current value
                
        if (flag == 1):               # if the type is a voltage source
            result_a = y_add          # pass the matrix A to result_a for preparing output
            result_c = currents       # pass the matrix C to result_c for preparing output
            dim_a = max_nodes + 1     # Since there's dimension changed for a voltage source, update new dimension for matrix A
            dim_c = max_nodes + 1     # Since there's dimension changed for a voltage source, update new dimension for matrix C
            
        else:                         # if the type is a current source
            result_a = y_add          # pass the matrix A to result_a for preparing output
            result_c = currents       # pass the matrix C to result_c for preparing output
            dim_a = max_nodes         # No dimension changed 
            dim_c = max_nodes         # No dimension changed
            
    return result_a, result_c, dim_a, dim_c  # return matrix A, matrix C, dimension of matrix A, dimension of matrix C

############################################################
# Start the main program now...                            #
############################################################

netlist = read_netlist()                            # Read the netlist!

# Print the netlist so we can verify we've read it correctly
for index in range(len(netlist)):
    print(netlist[index])
print("\n")

max_nodes = ranknetlist(netlist)                    # Call ranknetlist function to calculate the maximum nodes
matrix_a = np.zeros([max_nodes ,max_nodes])         # prepare a clean matrix with [maximum node x maximum nodes] for holding the stamp resistor matrix values
#print(matrix_a)                                    # DEBUG PRINT
matrix_c = np.zeros([max_nodes ,1])                 # prepare a clean matrix with [maximum node x 1] for holding the stamp current matrix values
#print(matrix_c)                                    # DEBUG PRINT

updated_a = np.zeros([max_nodes + 1,max_nodes +1])  # prepare a clean matrix for holding the calculated resistor matrix values
updated_c = np.zeros([max_nodes + 1,max_nodes +1])  # prepare a clean matrix for holding the calculated resistor matrix values

# Now call the stamper function to stamp the values from the netlist
# store the return matrices and its dimensions
[updated_a, updated_c,dim_a,dim_c] = stamper(matrix_a, netlist, matrix_c, max_nodes)

#print(updated_a)                                   # DEBUG PRINT
#print(updated_c)                                   # DEBUG PRINT

    
voltage = solve(updated_a, updated_c)               # solve for the X matrix. (AX = C)
print(voltage)                                      # print the solved result


