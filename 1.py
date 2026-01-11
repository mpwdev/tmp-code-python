import csv

people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

# for i in people:
# 	print(i)
# 	for b in i:
# 		print(b)

with open('people1.csv', 'w') as f:
	writer = csv.writer(f, lineterminator='\n')
	for row in people:
		writer.writerow(row)

with open('people1.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
