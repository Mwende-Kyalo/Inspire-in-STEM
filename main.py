#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :06/ 06/ 2022 
#    File :main.py
##################################### 

import operations
from student import student
from teachers import Teachers
from classes import Classes
 
print(operations.add_numbers(5,6))
print(operations.subtract_numbers(9,7))
print(operations.multiply_numbers(7,80))
print(operations.divide_numbers(50,10))


new_student = student("Tiffah","sleeping",2004)
new_teacher = Teachers("Mr.Mathenge",5829248,"Photography",60000)

student.greet_student()
print(new_teacher.get_tsc_no())
