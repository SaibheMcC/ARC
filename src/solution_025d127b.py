import sys #import the sys library
import json #import the json library


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

        #while count is less than the length of the data
        i= 0
        count = len(data[value])
        #print (count)
        while i < count:

            #Access first input
            input = data[value][i]['input']
            #print (i, count, value, input)
            
            #insert 0 at element 0
            input[1].insert(0, 0)
            #remove last index
            del input[1][-1]


            #check if there is more than 10 rows of data
            #if there more than 10 rows, process a second shape
            if len(input) > 10:
                #last row of data is saved to sub_list
                sub_list = input[-1]
                #insert sub_list
                input.insert(6, sub_list)
                #remove last row
                del input[-1]

                #last row of data is saved to sub_list
                sub_list = input[-1]
                #insert 6 into sub_list
                input.insert(6, sub_list)
                #remove last row
                del input[-1]
                
                
            #print (len(input))
            #print(input)
            i +=1

solve()         
        