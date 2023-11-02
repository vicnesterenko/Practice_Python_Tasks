import math
from abc import ABC, abstractclassmethod


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

    def __str__(self):
        return "\n".join(
            [
                "Your calculations are ready:",
                f"Shape: Rectangle",
                f"Length: {self.length}",
                f"Width: {self.width}",
                f"Perimeter: {self.calculate_perimeter()}",
                f"Area: {self.calculate_area()}",
            ]
        )


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return "\n".join(
            [
                "Your calculations are ready:",
                "Shape: Circle",
                f"Radius: {self.radius}",
                f"Perimeter: {self.calculate_perimeter()}",
                f"Area: {self.calculate_area()}",
            ]
        )


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def calculate_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def calculate_area(self):
        half_perimeter = self.calculate_perimeter() / 2
        return math.sqrt(
            half_perimeter
            * (half_perimeter - self.side_1)
            * (half_perimeter - self.side_2)
            * (half_perimeter - self.side_3)
        )

    def type_triangle(self):
        if (
            (self.side_1 + self.side_2 > self.side_3)
            and (self.side_1 + self.side_3 > self.side_2)
            and (self.side_2 + self.side_3 > self.side_1)
        ):
            if self.side_1 == self.side_2 == self.side_3:
                return "equilateral"
            elif (
                self.side_1 == self.side_2
                or self.side_1 == self.side_3
                or self.side_2 == self.side_3
            ):
                return "isosceles"
            else:
                return "scalene"
        else:
            return "Triangle doesn't exist! Input another sides."

    def __str__(self):
        return "\n".join(
            [
                "Your calculations are ready:",
                "Shape: Triangle",
                f"Side 1: {self.side_1}",
                f"Side 2: {self.side_2}",
                f"Side 3: {self.side_3}",
                f"Type of triangle: {self.type_triangle()}",
                f"Perimeter: {self.calculate_perimeter()}",
                f"Area: {self.calculate_area()}",
            ]
        )


def main():
    while True:
        shape_type = input("Write shape type for calculations or 'quit' to exit: ")
        if shape_type == "quit":
            break
        elif shape_type == "triangle":
            side_1 = abs(float(input("Enter side 1 of your triangle: ")))
            side_2 = abs(float(input("Enter side 2 of your triangle: ")))
            side_3 = abs(float(input("Enter side 3 of your triangle: ")))
            triangle = Triangle(side_1, side_2, side_3)
            print(triangle)
        elif shape_type == "circle":
            radius = abs(float(input("Enter the radius: ")))
            circle = Circle(radius)
            print(circle)
        elif shape_type == "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            rectangle = Rectangle(length, width)
            print(rectangle)
        else:
            print("This shape is not supported in our program! Please try again!")
            continue


if __name__ == "__main__":
    main()
