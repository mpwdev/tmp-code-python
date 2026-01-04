
class RobotTest:
	"""Test class for robot functionality"""
	def __init__(self, name="Robo", year=2024):
		self.name = name
		self.year = year
	
	def __del__(self):
		print(f'Robot {self.name} is being destroyed')

r1 = RobotTest('R1', 2025)
#print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__dict__)