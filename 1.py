
from math import isclose
# isclose()
x = 0.0000001
y = 0.0000002
print(x == y)
print(isclose(x, y, abs_tol=0.01))

a = 9999999999.01
b = 9999999999.02
print(isclose(a, b, rel_tol=0.01))

c = 4.5
d = 6.7
print(format(c + d, '.2f'))
