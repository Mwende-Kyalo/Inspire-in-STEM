#!/usr/bin/python 
#################################### 
#    Name : Mwende
#    Date :02/ 06/ 2022 
##################################### 

class Person:
    def _init__(self, _name, _age):
        self.name= _name
        self.age= _age

    def sayHi(self):
        print('Hello, my name is ' + self.name + ' and i am ' + str(self.age)+ ' years old')
#person1
person1 = Person('Bob', 16 )
person1.sayHi()

#person2
person2 = Person('Angie',18)
person2.sayHi()


