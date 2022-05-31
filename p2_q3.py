# Practical 2
# Q3

# Calculates the area of a rectangle
def calculateAreaOfRectangle(height, width):
    return height * width

# Calculates the area of a square
def calculateAreaOfSquare(height):
    return height * height

# Calculates the area of a triangle
def calculateAreaOfTriangle(height, base):
    return height * base / 2

# Asks for height, width and base
height = float(input("Insert Height Value: "))
width = float(input("Insert Width Value: "))
base = float(input("Insert Base Value: "))

# Prints the results after computing
print("Area of Rectangle = %.2f square meters" % calculateAreaOfRectangle(height, width))
print("Area of Square = %.2f square meters" % calculateAreaOfSquare(height))
print("Area of Triangle = %.2f square meters" % calculateAreaOfTriangle(height, base))
