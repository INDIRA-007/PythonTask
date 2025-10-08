#multithreading
#it is a process of executing multiple threads simultaneously
#thread is a lightweight process
#thread is a smallest unit of processing
#thread is a part of process
#thread is a separate flow of execution
#thread is used to perform multiple tasks simultaneously
#thread is used to improve performance of the application
# 1. create a thread
# 2. start a thread
# 3. wait until thread completes
# 4. run multiple thread simultaneously

import time
import threading
def printNum():
    for i in range(0,100):
        print(i)
        time.sleep(1)

s = "Hi Helo Welcome to python session!!!"
def printStr():
    for i in s:
        print(i)
        time.sleep(1)

# printNum()
# printStr()
t1 = threading.Thread(target=printNum).start()
t2 = threading.Thread(target=printStr).start()