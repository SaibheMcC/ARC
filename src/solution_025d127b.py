import json
data = json.load(open("/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/025d127b.json"))
data

set_values = ['train', 'test']

for value in set_values:

#iterate over set
    i= 0
    count = len(data[value])
    #print (count)
    while i < count:

    #Access first input
        my_list = data[value][i]['input']
        print (i, count, value, my_list)
        
        #insert 0 at element 0
        my_list[1].insert(0, 0)
        #remove last index
        del my_list[1][-1]
        
        if len(my_list) > 10:
            sub_list = my_list[-1]
            #insert sub_list
            my_list.insert(6, sub_list)
            #remove last row
            del my_list[-1]

            sub_list = my_list[-1]
            my_list.insert(6, sub_list)
            del my_list[-1]
            
            
        print (len(my_list))
        print(my_list)
        i +=1
        