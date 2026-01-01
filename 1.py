
def say_hello(name):
	"""This is custom function description - docstring"""
	print(f'Hello, {name}')
	
say_hello('Dan')
help(say_hello)
print(say_hello.__doc__)