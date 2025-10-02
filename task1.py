#task1
#Print the numbers 1 – 10, each on its own line, using a for loop.
for num in range(1,11):
    print(num)

print("\n")

#task2
#Use a while loop to accumulate and print the total of 1 + 2 + … + 100.
i=1
total=0
while(i<=100):
    total = total + i
    i = i + 1
print("Total is: ", total)

print("\n")

#task3
#Print all even integers from 2 to 50 inclusive in a single line, separated by spaces.

for i in range(2, 51):
    if(i % 2 == 0):
        print(i, end=" ")

print("\n")

#task4
#Ask the user for a starting number n and count down to 0, pausing one second between prints (time.sleep(1)).
import time
numInput = int(input("Enter a number: "))
for i in range(numInput, -1, -1):
    if(i >= 0):
        print(i)
        i = i - 1
        #time.sleep(1)
    else:
        print("Enter a number greater than zero")
print("\n")

#task5
#Read an integer ≥ 2 and print "Prime" or "Composite". No helper functions—just nested loops and break.

numInt = int(input("Enter a number: "))
for i in range(2, numInt):
    if(numInt % i == 0):
        print("Composite")
        break
else:
    print("Prime")

print("\n")