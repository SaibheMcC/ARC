#Name: Saibhe McCullough
#ID: 19234817
#PTAI Assignment 3


import sys #import the sys library
import json #import the json library
import numpy as np #import the numpy module

#solve function
def solve():

    #set datalocation to the argument passed in from the command line
    datalocation = sys.argv[1]

    #open datalocation, and load it into variable data
    data = json.load(open(datalocation))

    # list of set values (train set or test set)
    set_values = ['train', 'test']

    #iterate over set
    for value in set_values:

        #while count is less than the length of the data set
        i = 0
        count = len(data[value])
        while i < count:

            #access input i
            input = data[value][i]['input']
            #create structure output
            output = input
            
            #iterate through each row
            for row in output:
                 #insert zero at element 0
                row.insert(0,0)
                #remove last index
                del row[-1]
        
           #if there are more than 10 rows of data
            if len(output) > 10:
                #sublist captures rows 12 onwards
                sub_list = output[12:]
               #insert sub_list at row 6
                output.insert(6, sub_list)
                #remove rows 12 onwards
                del output[12:]

            #create a numpy array out of the output
            output = np.array([output])
            #print statement to print each output grid as numbers and spaces
            print(*output.flatten(), sep=' ')
            i +=1

solve()         
        