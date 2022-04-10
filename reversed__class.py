class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __reversed__(self):
        return self.name[::-1]


name = input('enter name : ')
age = int( input('enter age : ') )

p1 = Person(name, age)

print('reversed p1 is ', reversed(p1))
