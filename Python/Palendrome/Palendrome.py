import random,time
from num2words import *
from img import *
pallendrome = []
notPallendrome = []
for i in range(100,1000):

  for j in range(i,1000):
    equales = print(i,'*',j, '=' , j * i)
    result = str(j*i[::-1])
    print(result)
    break;
    if i == j:
      pallendrome.append(str(equales))
    else:
      notPallendrome.append(equales)
      
