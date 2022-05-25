#!/usr/bin/python 

#################################### 
#    Dictionaries 
#    Name : Mwende
#    Date :23/ 05/ 2022 
##################################### 


# Initializing dictionaries 
student = {"Name":"RuPaul","Age":56,"Gender":"Female"}
print(student["Name"])
print(student["Age"]) 
print(student["Gender"]) 

student[" Id-No"] = "896552336"
student["Hobby"] = "sleeping"
student["Football"] = "Man-city" 
student["fav_food"] = "Chakula" 
student["homeCity"] = "Home"
print(student) 

#modifying values 
student["Name"] = "Joe"
student["Age"] = 23
print(student) 

#deleting values 
del student["fav_food"]
print(student)