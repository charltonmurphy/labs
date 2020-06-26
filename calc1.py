import math
from array import *

def add(a, b, c, d):
    return(a+b+c+d)

def subtract(a, b, c, d,):
    return(a-b-c-d)

def multiply(a, b, c, d,):
    return(a*b*c*d)

def divide(a, b, c, d):
    return(a/b/c/d)



a = 8
b = 4
c = 2
d = 1
num = int(input(" Please give me a number between 1 and 4: "))


arr = []

for i in range(4):
    x = int(input("Enter a whole  number: "))
    arr.append(x)
if arr[0] == 0 or []:
    arr[0] = 8
if arr[1] == 0 or []:
    arr[1] = 4
if arr[2] == 0 or []:
    arr[2] = 2
if arr[3] == 0 or []:
    arr[3] = 1

a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]
   
print (arr)


if num == 1:
    print (add(a, b, c, d))
elif num == 2:
    print (subtract(a, b, c,d))
elif num == 3:
    print (multiply(a, b, c, d))
elif num == 4:
    print (divide(a, b, c, d))
elif num >= 5:
    print ('You number is too high')
elif num == 0:
    print ('No dude that is too low')
elif num == []: 
    print ("YOU ARE A DUMBASS!!!!")








