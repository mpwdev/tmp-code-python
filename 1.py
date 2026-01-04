with open('sample_file.txt', 'r') as f:
	content = f.read().splitlines()
	content = '\n'.join(content)

print(content)

