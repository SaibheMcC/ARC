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

    #put the result values together so that they become a list of coordinates. 
    #These coordinates can be used to locate where the 3 values are in the grid 
    listOfCoordinates= list(zip(result[1], result[2]))
    listOfCoordinates

    #i = 0
    #while i <=len(listOfCoordinates):
    current_coord = listOfCoordinates[0]
        #next_coord = listOfCoordinates[i+1]
    print ('current', current_coord)
        #print ('next', next_coord)
        #pattern = current_cord[]
    current_coord
    #current_coord[0][0]
    #current_coord[0][0]
    listOfCoordinates[2][0] 

    print(current_coord[1])
    x = current_coord[0]
    y = current_coord[1]
    print (x,y)

    for coord in listOfCoordinates:
        current = coord
        
        #check for 3 in next row down, to the left
        if coord[0] == (x+1): 
           # print ('x left')
            if coord[1] < y:
              #  print ('Y left')
                print ('left', coord)
                left = coord
                
                #check for 3 on this row, to the right
                for coord in listOfCoordinates:
                    if coord[1] > y:
                      #  print ('Y on the right also')
                        print ('right', coord)
                        right = coord
                        for coord in listOfCoordinates:
                            if coord[0] == (x+2):
                                #print ('x on the bottom')
                                if coord[1] == y:
                                   # print ('Y on the bottom also')
                                    print ('bottom', coord)
                                    bottom = coord
                                    print (left, right, bottom)
                                    
                                    #need to find all locations in between current, left, right, bottom, and fill them in with a number
                
                
                
            
        else:
            print ('none found')

solve()            
