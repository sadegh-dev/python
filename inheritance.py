class Person:
    def __init__(self, name):
        self.name = name
        print(f'Create Person by name is {name}')


class User(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.username = email
        print(f'Create User by email is {email}')



e1 = User('charlie','charlie@email.com')
print(e1.name)
