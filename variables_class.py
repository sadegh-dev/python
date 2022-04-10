class User:
    counter = 0
    def __init__(self, counter):
        User.counter += 1
        self.counter = counter



u1 = User(10)
print(u1.counter)
print(User.counter)

print('-------------')

u2 = User(20)
print(u2.counter)
print(User.counter)