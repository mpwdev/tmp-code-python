
## Defining a class
class Circle:
    def __init__(self, radius):    # instance attribute
        self.radius = radius

    ## Define a  Magic Method that is automatically called when printing an object
    ## YOUR CODE STARTS HERE
    def __str__(self):
        return str(self.radius)


## Creating an instance called moon with radius 1737
moon = Circle(1737)

## Printing the moon object
print(moon)