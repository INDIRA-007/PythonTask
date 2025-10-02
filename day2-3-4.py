# variables

a = 10
b= 69.56
c = "Indira"
print("Value of a is", a)
print("Type of a is", type(a))

print("Value of b is", b)
print("Type of b is", type(b))

print("Value of c is", c)
print("Type of c is", type(c))

print("Enter the value of d :")
d = input()
print("Value of d is", d)
print("Type of d is", type(d))
d = int(d)
print("Type cast Value of d is", type(d))

# variable name = a
# variable type = int
# variable size = 

# rule -> start with alphabet or _, lowercase or uppercase, no special char except _
# data -> int float str bool list tuple set dict
list1 = [10, 20.5, "Indira", True]
# list -> ordered, indexed, mutable, allows duplicate
tuple1 = (10, 20.5, "Indira", True)
# tuple -> ordered, indexed, immutable, allows duplicate
set1 = {10, 20.5, "Indira", True}
# set -> unordered, unindexed, mutable, no duplicate
dict1 = {"a": 10, "b": 20.5, "c": "Indira", "d": True}
# dict -> unordered, indexed, mutable, no duplicate, key:value pair


# class 3

# operators
#Arithematic -> +, -, *, /, %, //, **
# comparative -> >, <, >=, <=, ==, != 
# logical -> and, or, not

# conditional statements
# if, if-else, if-elif-else, nested if
print("\n")
val1 = int(input("Enter the value of val1 :"))
val2 = int(input("Enter the value of val2 :"))

if(val1 != 0):
    print("Value of val1 is not zero: ", val1)
elif(val1 == val2):
    print("Value of val1 is equal to val2: ", val1 , val2)
else:
    print("Value of val1 is zero: ", val1)

print("\n")
# loops
#while -> condition
n=0
while(n<=10):
    n = n+1
    if(n==5):
        continue
    if(n==8):
        break
    print("Value of n is: ", n)
print("\n")

# class 4
#for -> range, list, tuple, set, dict
s="good morning"
l =["1","3","5","7","9"]
t = (2,4,6,8,10)

for a in range(1,11):
    print("Value of a using range is: ", a)
print("\n")

for i in s:
    print("Value of i using string is: ", i)
print("\n")

for j in l:
    print("Value of j using list is: ", j)
print("\n")

# to delay the execution -> sleep
import time
for k in range(0,10):
    print(k)
    # time.sleep(3)



# function -> predefined, user defined
def printNum():
    """This is a function to print numbers"""
    print("test1")
    print("test2")
printNum()

def func1(a,b):
    """This is a function to add two numbers"""
    c = a + b
    return c
print(func1(1,2))

l=10
def printL():
    l=6
    return l
print("Local value: ",printL())
print("Global value: ",l)


# object(Class)