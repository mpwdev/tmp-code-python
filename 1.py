with open('configuration.txt') as f:
	content = f.read().splitlines()
	print(content)
print('-' * 30)

with open('configuration.txt') as f:
	content = f.readlines()
	print(content)
print('-' * 30)

with open('configuration.txt') as f:
	content = f.readline()
	print(content, end='')
	content = f.readline()
	print(content, end='')
print('-' * 30)

with open('configuration.txt') as f:
	content = list(f)
	print(content)
print('-' * 30)

with open('configuration.txt') as f:
	for line in f:
		print(line, end='')
print('')
print('-' * 30)