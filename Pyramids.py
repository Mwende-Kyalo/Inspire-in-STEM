#!/usr/bin/python
#################################### 
#    Name : Mwende
#    Date :27/ 05/ 2022 
##################################### 

rows = int(input("Enter the number of rows  "))
k = 0 
for i in range(1,rows+1):
    for space in range(1, (rows - i )+1 ):
        print(end="")
    while k != (2*i-1):
        print("*", end = "")
        k +=1
    k=0
    print( )
