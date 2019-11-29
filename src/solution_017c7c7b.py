import json #import the json library

def solve():

    d = json.load(open("/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/017c7c7b.json"))

    # list of set values (train set or test set)
    set_values = ['train', 'test']

    #iterate over each value in set_values
    for value in set_values:

        #while the count is less than the length of the set (training set or test set)
        i = 0
        count = len(d[value])
        while i < count:

            #access input i of each set
            input = d[value][i]['input']

            #iterate over input values
            #change values of 1's to 2's
            for row in input:
                for column in row:
                    if row[column] == 1:
                        row[column] = 2
            
            #get second half of data and append it onto the end of the data (this needs to be more specific - and capture 3 rows, but not the last row)
            sub_list = input[int(len(input)/2):]

            for x in sub_list:
                input.append(x)
            print (value, input)    
        
            i+=1 
            
solve()            