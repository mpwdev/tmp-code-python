
a = 0.1 * 3
b = 0.3
print(a == b)  # This will print False due to floating-point precision issues
print(format(a, '0.2f') == format(b, '0.2f'))  # This will print True
print(round(a, 2) == round(b, 2))  # This will also print True