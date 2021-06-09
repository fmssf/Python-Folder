import numpy,pandas,time,copy
from img import *

'''create 3 arrays, one to hold temp items coming in, one to hold parent number
and one to hold child numbers.'''
textFile = open("numbers.txt","r")
lines = textFile.readlines()

tmp = []
parent = []
child = []
'''
The for loop below will compare the current row with the row above it.
The following snipit of code will prepare row below before the loop starts.
It reads in and turns the entries from strings to numbers
- grabs the last line in the txt file
'''
tmp = lines[len(lines)-1].strip().split(' ')
for i in tmp:
  child.append(int(i))

''' walk the throug the text file from the bottom up. start with the second line from the bottom.'''
for i in range(len(lines)-2,-1,-1):
  
  #grabs a line and add it to the parent
  tmp = lines[i].strip().split(' ')
  parent = []
  for j in tmp:
    parent.append(int(j))
  
  for j in range(0,len(parent),1):
    if child[j] > child[j+1]:
      parent[j] += child[j]
    else:
      parent[j] += child[j+1]

  child = []
  child = parent.copy()
  
print(parent[0])

'''
  Walk through every row of the triangle except the last. The last was prebuilt
'''



'''
            {
                # Grab the next row up the triangle as the parent
               


                # Walk through each item in the parent and add the largest adjacent item from the child
                for ()
                {
                    # Turn it into a number 
                    


                    # Add the larger of the two adjacent numbers
                    if () {
                        
                    }
                    else
                    {
                        
                    }
                }


                # Overwrite the child array with the parent array; child becomes parent for next run 
                childNums = new int[tempItems.Length];
                parentNums.CopyTo(childNums, 0);
'''
