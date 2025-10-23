#inbuild modules
#time, os, sys, threading, math, random, datatime, 
#external modules
#pyexcel, numpy, pandas, matplotlib, 
#seaborn, sklearn, tensorflow, keras, pytorch,openssl, flask, django


# to install external modules
# pip install module name
# pip uninstall module name
# pip list


class Student:
    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayStudent(self):
        return f"Name: {self.name}, Age:{self.age}, Gender:{self.gender}"
    
s1 = Student("John",25,"Male")
s2 = Student("Jane",22,"Female")
print(s1.displayStudent())
print(s2.displayStudent())