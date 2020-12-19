
def myFunc(thing):
    return thing % 3 == 0

a = [1,2,3,4,5,6,7,8,9]

print(list(filter(myFunc, a)))