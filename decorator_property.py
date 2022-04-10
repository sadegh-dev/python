class User:
    def __init__(self, name):
        self.name = name
    
    @property
    def get_email(self):
        return f'{self.name}@email.com'

u1 = User('katty')

print(u1.get_email)