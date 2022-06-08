#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :30/ 05/ 2022 
##################################### 
 
#write a program to check if a number is divisible by 5 or 7
number = int(input("Enter the number :"))
if (number %7 ==0) and and (number %5 ==0):
        print(f"The number {number} is divisible by 7 and 5") 
else:
    print(f"The number {number} is not divisible by both 5 and 7")