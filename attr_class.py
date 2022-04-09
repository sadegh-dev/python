class Person :
    def __init__(self, name):
        self.name = name


p1 = Person('charlie')
p1.lname = 'kroger'
p2 = Person('katty')


print( getattr(p1, 'lname') )

print( getattr(p2, 'name') )
