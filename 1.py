
list_orig = [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]

def list_uniq(list_to_uniq):
	t1 = set(list_to_uniq)
	t2 = list(t1)
	return t2

n = list_uniq(list_orig)

print(n)