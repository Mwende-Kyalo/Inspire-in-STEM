#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :27/ 05/ 2022 
##################################### 


number = int(input("Enter the number"))
factorial = 1
if number < 0:
    print("Factorial of negative numbers does not exist")

elif number == 0:
    print("Factorial of 0 = 1") 

else :
    for i in range(1,number +1):
        factorial = factorial * i 
print("factorial of number " ,factorial)

