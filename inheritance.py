class Person:
    def __init__(self, name):
        self.name = name
        print(f'Create Person by name is {name}')


class User(Person):
    def __init__(self, email, name):
        super().__init__(name)
        self.username = email
        print(f'Create User by username is {email}')



e1 = User()