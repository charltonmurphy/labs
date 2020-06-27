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

num = (input(" Please give me a number between 1 and 4: "))
if (num >= '5'):
    print ('Your number is too high please restart')
elif (num <= '0'):
    print ('No dude, that is too low, or its not a number, please restart')
else:

    arr = []

    for i in range(4):
        x = (input("Enter a whole  number: "))
        arr.append(x)
    if arr[0] == "":
        arr[0] = 8
    if arr[1] == "":
        arr[1] = 4
    if arr[2] == "":
        arr[2] = 2
    if arr[3] == "":
        arr[3] = 1

    a = int(arr[0])
    b = int(arr[1])
    c = int(arr[2])
    d = int(arr[3])
   
    print (arr)


    if num == '1':
        print (add(a, b, c, d))
    elif num == '2':
        print (subtract(a, b, c,d))
    elif num == '3':
        print (multiply(a, b, c, d))
    elif num == '4':
        print (divide(a, b, c, d))
    








