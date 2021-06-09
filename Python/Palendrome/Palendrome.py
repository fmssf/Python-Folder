import random,time
from num2words import *
from img import *
Pallendrome=open("pallendrome.txt", "a")
NotPallendrome = open("NotPallendrome.txt","a")
pallendrome = []
notPallendrome = []
#print(pallendrome) 
for i in range(100,1000):

  for j in range(i,1000):
    equales = i * j
    output = str(equales)
    revers = output[::-1]
    if revers == output:
      pallendrome.append(revers)
      for i in pallendrome:
        print(i,file=Pallendrome,end="\n")
        if int(revers) > 0:
          print(output)
          break;
      break;
     

    else:
      notPallendrome.append(output)
     
      for i in notPallendrome:
        print(i,file=NotPallendrome,end="\n")
        break

    

    

'''
pallendrome.append(revers)
print(pallendrome)
'''  
     
