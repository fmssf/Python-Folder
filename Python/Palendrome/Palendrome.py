import random,time
from num2words import *
from img import *

while True:
  num1 = random.randint(100,999)
  output = num1 * num1
  print(num1 , "*" ,num1 ,"=", output)
  time.sleep(1)
  
