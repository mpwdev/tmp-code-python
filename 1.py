
user = {'username': 'js', 'level': 'admin33'}

def only_admin(func):
	def wrapper_only_admin(*args, **kwargs):
		if user['level'] == 'admin':
			return func(*args, **kwargs)
		else:
			raise PermissionError("User does not have admin privileges")
	return wrapper_only_admin

# # decorator example
# def user_has_permission(func):
# 	def wrapper_user_has_permission():
# 		if user['level'] == 'admin':
# 			return func()
# 		else:
# 			return None
# 	return wrapper_user_has_permission

@only_admin # @ syntax
def show_pass():
	return "password123"

# try:
# 	my_function = only_admin(show_pass)
# 	print(my_function())
# except PermissionError as e:
# 	print(e)

try:
	show_pass()
except PermissionError as e:
	print(e)