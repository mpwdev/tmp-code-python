import json
friends = {'Dan': [20, 'London', 3234342], 'Maria': [22, 'New York', 9876543]}

with open('friends.json', 'w') as f:
	json.dump(friends, f)

	json_string = json.dumps(friends, indent=4)
	print(json_string)
