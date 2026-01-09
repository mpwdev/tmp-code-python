
user = {'username': 'js', 'level': 'admin33'}

# decorator example
def user_has_permission(func):
	if user['level'] == 'admin':
		return func
	else:
		return None
	
def show_pass():
	return "password123"

my_function = user_has_permission(show_pass)
if my_function != None:
	print(my_function())
else:
	print('No access')