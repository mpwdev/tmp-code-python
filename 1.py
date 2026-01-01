
# names = {'tom', 'ANNE', 'John', 'dAn'}
# print(id(names))
# names = {n.capitalize() for n in names}
# print(id(names))
# print(names)

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {k*2: v*2 for k,v in d1.items()}
# print(d2)

# d3 = {k.upper(): v*2 for k,v in d1.items()}
# print(d3)

# d4 = {k.upper(): v*2 for k,v in d1.items() if v % 3 == 0}
# print(d4)

years = [2020, 2021, 2022]
revenues = [10000, 50000, 10000]
z = zip(years, revenues)
#print(z)
sales = list(z)
print(sales)

sales_dict = dict(zip(years, revenues))
print(sales_dict)

profit = {k: v*0.15 for k,v in sales_dict.items()}
print(profit)
