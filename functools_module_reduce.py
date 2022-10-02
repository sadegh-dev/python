from functools import reduce

nums = [10,20,30]

def add(a,b):
    return a+b


print(reduce(add,nums))

