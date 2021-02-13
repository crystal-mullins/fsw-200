import sys
from random import*
a=randrange(1,9)
b = 0
guesses = 0 #Initialize a variable to store how many guesses the user has used
while b != a:
        x = "exit"
        b=int(input("Can you guess my number?: "))
        if a>b:
        b=int(input("Too low, try again: "))
        else:
        b=int(input("Too high, try again: "))

    while x = "exit":
    answer = input('Do you want to continue?:')
    if answer.lower().startswith("y"):
      print("ok, carry on then")
    elif answer.lower().startswith("n"):
      print("ok, sayonnara")
      exit()

    b=int(input("Can you guess my number?: "))
    if a>b:
        b=int(input("Too low, try again: "))
    else:
        b=int(input("Too high, try again: "))
    guesses+=1
    

print("You got it! The number was", a)
print("You took {} guesses!".format(guesses))