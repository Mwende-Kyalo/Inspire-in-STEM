#A dictionary is a collection of key value pairs
#syntax: dictionary = {'key':'value'} 
from turtle import color

names = 'Ada Lovelace'
colors={'color':'red'}
vehicles={'type':'toyota','plate number':'KYZ 001A'}
#print(type(colors)) #we use the type method to read the data type
# Accessing values of an element inside a dcitionary 
 
#print(vehicles['type'], vehicles['plate number']) #You can access the value of an element inside a dictionary 

#dictionary person
person ={'name':'Grandpa_Smurf','address':'00100','phone_number':'0700000000','gender':'AMAB'}
#person['age']='21'
#person['fav_colour']='White'
#print(type(person))
#print(person['age'])
#del person["phone_number"] 
#print(person)

#looping over dictionaries
for key, value in person.items():
    print(f"{key}:{value}")