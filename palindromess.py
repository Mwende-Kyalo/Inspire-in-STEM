#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :08/ 06/ 2022 
##################################### 

#program to check if a number or letter is a palindrome!
num=int(input("Enter a number:"))
words=input("Enter a string:")

temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


if(words==words[::-1]):
      print("The string is a palindrome!")
else:
      print("Not a palindrome!")


