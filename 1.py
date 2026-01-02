
with open('myfile.txt', 'w') as file:
	file.write('line number 1\n')
	file.write('line number 2')

with open('myfile.txt', 'a') as f:
	f.write('\nline number 3 appended\n')
	f.write('line number 4\n')

with open('myfile.txt', 'r+') as f:
	f.write('\nline number 5 appended\n')
	f.write('line number 6\n')

	print(f.read())

