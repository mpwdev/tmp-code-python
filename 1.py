import os
os.chdir('./dir2/')

i = 1
for file in os.listdir():
	#print(file)
	file_name, file_extension = os.path.splitext(file)
	#print(f'File Name: {file_name}, File Extension: {file_extension}')
	new_file_name = f'{str(i)}_{file_name}{file_extension}'
	print(new_file_name)
	i += 1

	print(f'Renaming {file} to {new_file_name}')
	os.rename(file, new_file_name)