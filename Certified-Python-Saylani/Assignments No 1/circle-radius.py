# Here we are importing pi from math library
from math import pi

# Here we are storing float value in radius
radius = float(input('Input the radius of the circle: '))

# Here we are converting radius variable into string and then multiplying pi into radius square
print('The area of the circle with radius ' + str(radius) + ' is: ' + str(pi * radius**2))