#!/usr/bin/python

#programme that gets the user input and adds ksh10,000 to her account if she is btn 25 - 30yrs 
age = input("How old are you ?")

acc_bal = 0 
if (int(age) > 25) and (int(age) < 30):
    acc_bal = acc_bal + 10000 
    print("Confirmed!You have received ksh. 10,000")
else:
    print("Sorry!No money for you.") 

