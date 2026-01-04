
def tail(filename, n=10):
	with open(filename) as f:
		content = f.read().splitlines()
		last = content[len(content)-n:]
		#print(last)
		my_str = '\n'.join(last)
		return my_str

t = tail('sample_file.txt', 5)
print(t)