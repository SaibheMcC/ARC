import json
import numpy as np

data = json.load(open("/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/00d62c1b.json"))
#data

#Access first input
my_list = data['train'][0]['input']
my_list

my_list = np.array([my_list])
result = np.where(my_list == 3)
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

   # i +=1