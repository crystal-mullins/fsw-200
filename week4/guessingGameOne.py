import random
a = random.randint(1,9)
b = " is the number"
num = int(input("Guess a number: "))
if (num == a) :
   print("{0} you guessed right YOU WIN".format(num))
else:
   print("{0} Sorry that is not the number YOU LOSE".format(num))
if (num > a) :
   print("{0} You guessed to high!".format(num))
elif (num < a):
   print("{0} You guessed to low".format(num))

print("{}{}".format(a,b))
