try:
    a = int(input("enter a"))
    print(10/a)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")

 #python debugger
#0
# pdb commands
# l - list where you are in the code
# n - next line
# c - continue execution
# q - quit debugger

import pdb
def add(a,b):
    pdb.set_trace() # set a breakpoint pdb
    return a+b
a = int(input("enter a"))
b = int(input("enter b"))
print(add(a,b))
