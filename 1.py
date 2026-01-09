def sum(number, fn):
	result = 0
	for i in range(1, number + 1):
		result += fn(i)
	return result

def square(x):
	#print(x, x ** 2)
	return x ** 2

result = sum(3, square)  # Should return 14
print(result)