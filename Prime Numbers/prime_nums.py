#This code is to find the next prime number of any number you provide. 

from array import *
x=0
j=1

def other_nums():
    global x
    global j
    for i in range(1, x):
        if (i == 1):
            if(x%i == 0):
                j+=1
        if (i > 1) and (i < x):
            if(x%i != 0):
                j+=1
            else:
                find_next()
        if (i == x):
            if(x%i == 0):
                j+=1
        if(j==x):
            answer()


def find_next():
    global x
    x+=1
    other_nums()

def start(y):
    global x
    x=y
    find_next()

def answer():
    global x
    print(x)

start(343487)
                
