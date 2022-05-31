#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :31/ 05/ 2022 
##################################### 

#lists 
fruits = ['mango','guava','lime','banana'] 

fruits[2] = 'apple'
print(fruits)

#tuple
new_fruits =('mango','guava','lime','banana')
#new_fruits [1] = 'apple'(brings an error)
print(new_fruits[2])

#examples:
cars = ('audi','bmw','vw','toyota')
cars = ('nissan','bmw','vw','toyota')
print(cars)

fav_foods =('chapati','ugali','rice','milk')

for fav_food in fav_foods :
    print(fav_food)
