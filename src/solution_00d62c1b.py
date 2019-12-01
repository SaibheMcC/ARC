#Name: Saibhe McCullough
#ID: 19234817
#PTAI Assignment 3


import sys #import the sys library
import json #import the json library
import numpy as np #import the numpy library

#solve function
def solve():

    #set datalocation to the argument passed in from the command line
    datalocation = sys.argv[1]

    #open datalocation, and load it into variable data
    data = json.load(open(datalocation))
    
    #Access first input array
    input = data['train'][0]['input']

    #create a numpy array from the input
    input = np.array([input])

    #locate the 3 values, and save them as result
    result = np.where(input == 3)

    #put the result values together so that they become a list of coordinates (grid locations). 
    #These coordinates can be used to locate where the 3 values are in the grid 
    listOfCoordinates= list(zip(result[1], result[2]))
   
    #iterate through the list of co-ordinates
    for coord in listOfCoordinates:
     
        #check for a 3 in next row down, to the left
        if coord[0] == (x+1): 
            if coord[1] < y:
               #assign co-ordinate to the variable 'left'
                left = coord
                
                #check for 3 on next row down from current co-oordiante
                for coord in listOfCoordinates:
                    if coord[1] > y:
                        #assign co-ordinate to the variable 'right'
                        right = coord

                        #check for 3 on next row down from current co-oordiante
                        for coord in listOfCoordinates:
                            if coord[0] == (x+2):
                                if coord[1] == y:
                                    #assign co-ordinate to the variable 'bottom'
                                    bottom = coord

                                    #in the case that there is green squares, surrounding 1 or more black square
                                    #the program needs to change the value of the sqaure, so that it is yellow
                                           
            
        else:
            #if there is no green sqaures to create the shape, do nothing
            pass

solve()            
