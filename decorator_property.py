class User:
    def __init__(self, name):
        self.name = name
    
    @property
    def get_email(self):
        return f'{self.name}@email.com'

