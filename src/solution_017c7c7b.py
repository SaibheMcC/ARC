import json #import the json module
import sys #import the sys module
import numpy as np #import the numpy module


#solve function
def solve():

    #set datalocation to the argument passed in from the command line
    datalocation = sys.argv[1]

    #open datalocation, and load it into variable data
    data = json.load(open(datalocation))

    # list of set values (train set or test set)
    set_values = ['train', 'test']

    #iterate over each value in set_values
    for value in set_values:

        #while the count is less than the length of the set (training set or test set)
        i = 0
        count = len(data[value])
        while i < count:

            #access input i of each set
            input = data[value][i]['input']
            #create a new structure, output
            output = input

            #iterate over input values
            #change the blue squares to red
            #by swapping any values of 1 to become 2
            for row in output:
                for column in row:
                    if row[column] == 1:
                        row[column] = 2
                        #print (row[column])
            
            #sub_list = get first half of data and append it onto the end of the data
            sub_list = output[:int(len(output)/2)]

            #iterate through each item in the sub_list
            for x in sub_list:
                #append the each item to the input data
                output.append(x)

            #create a numpy array out of the output
            output = np.array([output])
            #print statement to print each output grid as numbers and spaces
            print(*output.flatten(), sep=' ')

            #add 1 to i
            #this is th counter for the while loop
            i+=1 
                  
            
solve() #call the solve function           