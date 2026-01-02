
# f = open('configuration.txt')
# content = f.read(5)
# print(content)

# content = f.read(3)
# print(content)

# print(f.tell())

# f.seek(2)
# content = f.read(3)
# print(content)
# print(f.tell())

# f.close()

f = open('configuration.txt')
print(f.read())
f.close()

f = open('configuration.txt')
print('#' * 20)
#f.seek(0)
print(f.read())
f.close()
