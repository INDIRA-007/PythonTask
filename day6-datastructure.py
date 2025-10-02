# data structure
# list, tuple, set, dictionary

ls = ["val1","val2","val3"]
ls1 = ["val1","val2","val3"]
print(ls)

for i in ls:
    print(i)

# 1. Indexing
# 2. Operators
  # +, *, in, not in

print(ls + ls1)
print(ls * 2)
print(ls[2])
print(ls[:2])
print("val2" in ls)
print("val2" not in ls)
ls2 = [1,2,3,4,50,98,00.87]
print(12 in ls2)
print(ls2[2:4])
out = ls2[(len(ls2)-3): ]
print(out)

ls3 = [1,2,3,4,5,6,7,8,9,0]
print(ls3)
ls3[3] = "Python"
print(ls3)
ls3[7:]="45"
print(ls3)
ls3[8:] = ["45"]
print(ls3)
del ls3[3:]
print(ls3)

#len()
#max()
#min()
#sum()
#sorted()
lt = [7,8,9,5,64,78,1,47,2,0,6]
print("Sorrted List: ",sorted(lt))
#append()
lt.append(11)
print("Append 11 to the list: ",lt) 
#remove()
lt.remove(78)
print("Remove the value from the list: ",lt)
#insert()
lt.insert(2,100)
print("Insert the value at specific position: ",lt)
lt.insert(4,[8,6,5])
print("Insert the value at specific position: ",lt)
#reverse()
lt.reverse()
print("Reverse the list: ",lt)
#count()
#list()
s = "Programming"
print("List the string: ",list(s))