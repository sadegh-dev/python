class Person:
	def __init__(self, username, national_code, tell):
		self.username = username
		self.national_code = national_code
		self.tell = tell

	def __getattr__(self, item):
		return 'it is not exist...'

	def __getattribute__(self, item):
		if item == 'username':
			return "don't access."
		else:
			return super().__getattribute__(item)

	def __setattr__(self, key, value):
		if key == 'national_code' and len(value) != 10:
			print( 'value is wrong.' )
		else:
			return super().__setattr__(key,value)

	def __delattr__(self, key):
		if key == 'tell':
			print("you can't delete tell")
		else:
			return super().__delattr__(key)




p1 = Person('char123', '2003400005','09121002030')



print(p1.username)
#don't acces.

p1.national_code = '2030'
#value is wrong

del p1.username

