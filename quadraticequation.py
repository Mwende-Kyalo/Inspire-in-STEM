#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :31/ 05/ 2022 
##################################### 

# a is the co-efficient of the first term
# b is the co-efficient of the second term
# c is the constant
from math import sqrt

a = int(input("Enter the co-efficient of the first term(a) ")) 
b = int(input("Enter the co-efficient of the second term(b) ")) 
c = int(input("Enter the constant (c) "))
def find_roots(a,b,c):
    y1 = (-b +sqrt((b **2) - 4*a*c )) / (2*a)
    y2 = (-b -sqrt((b **2) - 4*a*c )) / (2*a)
    print("The roots of the quadratic equation are :", y1,y2)
find_roots(a,b,c)

w = sqrt(b**2 - 4*a*c) 
def find_roots(a,b,c):
    y1 = (-b + w) / (2*a)
    y2 = (-b - w) / (2*a)
    print("The roots of the quadratic equation are :", y1,y2)
find_roots(a,b,c)

