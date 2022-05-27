#!/usr/bin/python 

for numbers in range(0,20):
    if(numbers %2 == 0):
        print(numbers)
 
 #sum of all even numbers between 0 and 50
sum = 0
for numbers in range(0,20):
    if(numbers %2 == 0):
        sum = sum +numbers 
print(sum)

#Product of all odd numbers between 0 and 20 
product = 1 
for numbers in range(1,20):
    if(numbers %2 == 1):
        product = product * numbers 
print(product) 

#calculate the factorial of 6 (6!)
prod = 1
for numbers in range(1,6):
    fact = numbers * (numbers-1)
print(fact) 

#while loops 
num = 0
while num <10 :
    print(num)
    num = num + 1 

num=0
while num <10 :
    if(num %2 == 0):
        print(num)
    num = num + 1


