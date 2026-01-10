
import functools
user = {'username': 'js', 'level': 'admin'}

def only_admin(func):
	@functools.wraps(func)
	def wrapper_only_admin(*args, **kwargs):
		'''
		------------
		Docstring for wrapper_only_admin
		
		:param args: Description
		:param kwargs: Description
		------------
		'''
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
	print('pass for admin xxxxxxx')
	return "password123"

# try:
# 	my_function = only_admin(show_pass)
# 	print(my_function())
# except PermissionError as e:
# 	print(e)

@only_admin
def create_user_and_group(user, group):
	print(f'This function create user {user} and group {group}')
	# code here

@only_admin
def update_system():
	'''
	Docstring for update_system
	'''
	print(f'This function update the OS')
	# code here

try:
	show_pass()
except PermissionError as e:
	print(e)

create_user_and_group('admin', 'sudo')
update_system()

print(update_system.__doc__)
print(update_system.__name__)