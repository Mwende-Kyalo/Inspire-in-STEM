#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :31/ 05/ 2022 
##################################### 


#defining a function(functions is a block of code which gets executed together )
def say_hello():
    print("Hello from JKUAT")
    x = 4 
    y = 7
    z = x + y 
    print(z)
say_hello() #calling the function

#animal sound
def bark():
    print("Dogs bark")
bark()
def meows():
    print("Cats meow") 
meows()
def neigh():
    print("Horses neigh") 
neigh()
def bray():
    print("Donkeys bray") 
bray()

# a function to add two numbers
def add_number(x,y): #x and y are the parameters
    sum_nums = x + y 
    print("The sum of numbers :", sum_nums)
add_number(40,50)
add_number(100,400)
add_number(1,4) 

# a function to multiply two numbers
def products(x,y):
    product_nums = x * y
    print("The product of the numbers is ", product_nums)
products(40,50)
    

def print_name(name = "Bob Marley"):
    print(name)
print_name("Jason")

#returning from a function 
def get_sum(num1,num2):
    sum_nums = num1 +  num2 
    return sum_nums
print(get_sum(7,12))

#get the square of numbers
def powers(number,power):
    pow_nums = number ** power 
    return pow_nums 
print(powers(6,4))

#printing ful names
def get_full_name(f_name , s_name):
    full_name = f_name + " " + s_name 
    return full_name.title()
print(get_full_name("Skip","Marley"))

# returning a dictionary from a function
def create_full_name(first_name,second_name):
    person{'first':'first_name','second':'second_name'}
    return person

    