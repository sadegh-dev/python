from functools import reduce

nums = [10,20,30,40,50]

def add(a,b):
    return a+b


print(reduce(add,nums,5))

