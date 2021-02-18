# print('functions')

# define a function

def funct1():
    print("I want to know what is going on")
    print("still in funct1")

funct1()

def square(x):
      	return x*x
print(square(4))

def multiply(x,y=0):
	print("value of x=",x)
	print("value of y=",y)
    
	return x*y
  
print(multiply(y=2,x=4))