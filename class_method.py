class User :
    def __init__(self, name):
        print(f'hello {name}')

    @classmethod
    def guest(cls):
        return cls('guest')

    @classmethod
    def admin(cls):
        return cls('admin')


User.guest()

User.admin()
