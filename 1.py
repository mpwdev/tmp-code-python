
def my_function(**kwargs):
	print(kwargs)
	for k, v in kwargs.items():
		print(f'k is {k} an v is {v}')

my_function(name='Bob', age=30, location = 'London', job='dev')

person = {'name':'Bobby', 'age':35, 'location': 'Berlin', 'job':'devvv'}
my_function(**person)

