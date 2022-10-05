#################
##### OOP #######
#################

from functools import singledispatchmethod

class Person:

    # single-dispatch generic function

    @singledispatchmethod
    def show(self, data1, data2):
        # default work
        raise NotImplementedError('Unsupported Type')


    # [Way1] Definition of the first type

    @show.register(str)
    @show.register(list)
    def navigation(self, this_data1, this_data2):
        for x in this_data1:
            print(x)


    # [Way2] Definition of the second type [Use type annotation]

    @show.register
    def simple_display(self, this_data1:int, this_data2):
        print(this_data1)



#### Main USE

p1 = Person()
p1.show('charlie', 53)









#################
### Function ####
#################

from functools import singledispatch


# single-dispatch generic function

@singledispatch
def show(data1, data2):
    # default work
    raise NotImplementedError('Unsupported Type')


# [Way1] Definition of the first type

@show.register(str)
@show.register(list)
def navigation(this_data1, this_data2):
    for x in this_data1:
        print(x)


# [Way2] Definition of the second type [Use type annotation]

@show.register
def simple_display(this_data1:int, this_data2):
    print(this_data1)






#### Main USE

show('charlie',20)
show(300,20)

# Monitor the activation of various functions

print(show.dispatch(int))
print(show.dispatch(list))
print(show.dispatch(str))


# Monitor all performance [OutPut is dictionary]

print(show.registry)

