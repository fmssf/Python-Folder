import numpy
import pandas
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
It reads in and turns the entries from strings to numbers'''
tmp = lines[len(lines)-1].strip().split(' ')
for i in tmp:
  child.append(int(i))
print(lines[1])


  # Walk through every row of the triangle except the last.  The last was prebuilt
'''for i, row in tmp.iterrows():
  print(f"Index: {i}")
  print(f"{row}\n")
'''
'''
for ()  
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
