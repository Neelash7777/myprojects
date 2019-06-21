#Making a digital dice without graphics.

from random import randint # importing random function to generate random number.
print("Give lower limit of dice")
x=int(input())
print("Give upper limit of dice")
y=int(input())
print("Type q to quit or any other key to continue")
while True:
    print(">>>"+str(randint(x,y))) #randint is to generate random numbers between x and y.
    if input()=='q': #if q is entered we come out of the loop.
        break