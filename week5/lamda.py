# adder = lambda x, y: x + y
# print (adder (11, 22))

# #What a lambda returns
# x='some kind of a useless lambda'
# (lambda x : print(x))(x)

# sequences = [10,2,8,7,5,4,3,11,0, 1]
# filtered_result = map (lambda x: x*x, sequences) 
# print(list(filtered_result))

# from functools import reduce
# sequences = [1,2,3,4,5]
# product = reduce (lambda x, y: x*y, sequences)
# print(product)

#  a function that takes one argument, and that argument will be multiplied with an unknown given number

def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))