#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :02/ 06/ 2022 
##################################### 

class Employee:
    def __init__(self, _name, _age, _salary):
        self.name= _name
        self.age= _age
        self.salary= _salary
    def sayHi(self):
        print('Hello, my name is ' + self.name + ' and i am ' + str(self.age)+ ' years old. I also earn ' + str(self.salary) + ' ksh. each month.')

#person1
person1 =Employee('Dan', 30, 50000)
person1.sayHi()

#person2
person1 =Employee('Esther', 28, 67000)
person1.sayHi()
