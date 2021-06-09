import random,time
from num2words import *
from img import *
pallendrome = []
notPallendrome = []
#print(pallendrome)
for i in range(100,1000):


  for j in range(i,1000):
    equales = i * j 

    output = i,"*",j,"=",equales
    revers = output[::-1]
    if revers == output:
      pallendrome.append(revers)
    else:
      notPallendrome.append(output)
    
    print(i)
'''
for j in range(i,1000):
    equales = i * j 
    output = i,"*",j,"=",equales
    revers = output[::-1]
    if revers == output:
      pallendrome.append(revers)
    else:
      notPallendrome.append(output)
    print(i,j)

  break;
'''
'''
pallendrome.append(revers)
print(pallendrome)
'''  
     
