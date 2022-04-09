
class Person :
    counter = 0
    def __init__(self):
        Person.counter += 1
        print(f'Person number {Person.counter}')

p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()



print(Person.__dict__['counter'])
