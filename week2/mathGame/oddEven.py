num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
if (num % 4) == 0:
   print("{0} is a multiple of 4".format(num))
else:
   print("{0} is not a multiple of 4".format(num))
   
num1 = int(input("Enter a number: "))
check = int(input("Enter a number: "))
if (num1 % check) == 0:
   print(f"{num1} divides evenly into {check}".format(num1))
else:
   print(f"{check} does not divide evenly into {num1}".format(check))