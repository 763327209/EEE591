############################################################
# Created on Fri Aug 24 13:36:53 2018                      #
#                                                          #
# @author: olhartin@asu.edu; updates by sdm                #
#                                                          #
# Program to solve resister network with a voltage source  #
############################################################

import numpy as np                     # needed for arrays
from numpy.linalg import solve         # needed for matrices
from read_netlist import read_netlist  # supplied function to read the netlist
import comp_constants as COMP          # needed for the common constants

# this is the list structure that we'll use to hold components:
# [ Type, Name, i, j, Value ] ; set up an index for each component's property

############################################################
# How large a matrix is needed for netlist? This could     #
# have been calculated at the same time as the netlist was #
# read in but we'll do it here to handle special cases     #
############################################################

def ranknetlist(netlist):              # pass in the netlist

    ### EXTRA STUFF HERE!

##    print(' Nodes ', nodes, ' total Nodes ', max_node)
    return nodes,max_node

############################################################
# Function to stamp the components into the netlist        #
############################################################

def stamper(y_add,netlist,currents,voltages,num_nodes): # pass in the netlist and matrices
    # y_add is the matrix of admittances
    # netlist is the list of lists to analyze
    # currents is the vector of currents
    # voltages is the vector of voltages
    # num_nodes is the number of nodes

    for comp in netlist:                            # for each component...
        #print(' comp ', comp)                       # which one are we handling...

        # extract the i,j and fill in the matrix...
        # subtract 1 since node 0 is GND and it isn't included in the matrix

        if ( comp[COMP.TYPE] == COMP.R ):           # a resistor
            i = comp[COMP.I] - 1
            j = comp[COMP.J] - 1
            if (i >= 0):                            # add on the diagonal
                y_add[i,i] += 1.0/comp[COMP.VAL]
            
            #EXTRA STUFF HERE!

    return num_nodes  # need to update with new value

############################################################
# Start the main program now...                            #
############################################################

# Read the netlist!
netlist = read_netlist()

# Print the netlist so we can verify we've read it correctly
for index in range(len(netlist)):
    print(netlist[index])
print("\n")

#EXTRA STUFF HERE!
