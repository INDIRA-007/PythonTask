# to perform any operations on files
# open, read, write, append, close
#f = open("sample.txt", "r")  # r, w, a, r+, w+, a+
# f = open("sample1.txt", "w")  # r, w, a
# f = open("sample1.txt", "a")  # r, w, a
# f = open("sample1.txt", "r+")  # r, w, a
# f = open("sample1.txt", "w+")  # r, w, a
# f = open("sample1.txt", "a+")  # r, w, a
# print(f)

# text -> only read and write in text format
# binary -> only read and write in binary format
# basic mode 
# write -> w
# read -> r
# append -> a
# w+ -> read and write
# r+ -> read and write
# a+ -> read and append
# f = open("sample.txt","a")
# f.write("\nhello hi Ind25\nHrw?.....")
# f.close()
f = open("sample.txt","r")
content = f.read()
content1 = f.readline()
content2 = f.readlines()
print(content)
print(content1)
f.close()

with open("sample.txt","r") as f:
    content = f.read()
    print(content)