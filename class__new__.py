class Person :
    def __init__(self, name):
        print(f'hello {name}')
    
    def __new__(cls, name, *args, **kwargs) :
        if name == 'katty' :
            return None
        else :
            return super().__new__(cls, *args, **kwargs)


u1 = Person('charlie')
u2 = Person('katty')

