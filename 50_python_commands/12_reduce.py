import functools

def myFunc(a,b):
    return a * b

# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 

print(functools.reduce(lambda a,b : a + b, lis))

print(functools.reduce(myFunc, lis))

print(functools.reduce(lambda a,b : a if a > b else b, lis))