#if()
# elif
# else

#error handling
#exception handling
# try
# except
# finally
a = 3
b = 0
if(b==0):
    print("Without Exception: Cannot divide")
else:
    print(a/b)

try:
    print(a/b)
except ZeroDivisionError:
    print("With Exception : Cannot divide")


# ZeroDivisionError  -> when denominator is zero
# NameError -> when variable is not defined
# IndexError -> when index is not present in the list
# KeyError -> when key is not present in the dictionary, key is case sensitive and should be in quotes
# ValueError -> when value is not valid, data type mismatch
# TypeError -> when data type is not supported for the operation
# IOError -> when file is not found 
# FileNotfounderror -> when file is not found
# FileExistsError -> when file already exists
# SyntaxError -> when syntax is not correct
# ModuleNotFoundError -> when module is not found
#indentation error -> when indentation is not correct

try:
    print(a/b)
except ZeroDivisionError as z:
    print("With Exception1 : Cannot divide -> ",z)
except NameError as n:
    print("Variable is not defined: ", n)
finally:
    print("This block is always executed")
