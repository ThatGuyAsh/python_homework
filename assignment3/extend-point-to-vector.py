# Task 5

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Equality method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Euclidean distance
    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )


class Vector(Point):

    # Uses the same __init__ as Point

    # Override string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Override + operator
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )


# Main program

# Create Points
point1 = Point(2, 3)
point2 = Point(5, 7)

print(point1)
print(point2)

# Test equality
print(point1 == point2)

# Test distance
print(point1.distance(point2))


# Create Vectors
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

print(vector1)
print(vector2)

# Test vector addition
vector3 = vector1 + vector2

print(vector3)

# Demonstrate Vector is also a Point
print(vector3.distance(point1))