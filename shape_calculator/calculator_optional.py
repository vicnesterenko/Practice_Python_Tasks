import math
from abc import ABC, abstractmethod

# math.dist(p, q) -> math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates.
# The two points must have the same dimension.


class Shape(ABC):
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    @abstractmethod
    def sides(self, point1, point2, point3):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, point1, point2, point3):
        super().__init__(point1, point2, point3)

    def sides(self, point1, point2, point3):
        side1 = math.dist(point1, point2)
        side2 = math.dist(point2, point3)
        side3 = math.dist(point3, point1)
        return side1, side2, side3

    def area(self):
        side1, side2, side3 = self.sides(self.point1, self.point2, self.point3)
        s = sum([side1, side2, side3]) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    def perimeter(self):
        side1, side2, side3 = self.sides(self.point1, self.point2, self.point3)
        return sum([side1, side2, side3])

    def type_triangle(self):
        side1, side2, side3 = self.sides(self.point1, self.point2, self.point3)
        if (
            (side1 + side2 > side3)
            and (side1 + side3 > side2)
            and (side2 + side3 > side1)
        ):
            if side1 == side2 == side3:
                return "equilateral"
            elif side1 == side2 or side1 == side3 or side2 == side3:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "Triangle doesn't exist! Input another sides."


def main():
    while True:
        shape_type = input("Enter shape type (triangle) or 'quit' to exit: ")
        if shape_type == "quit":
            break
        elif shape_type == "triangle":
            point1 = tuple(
                map(float, input("Enter coordinates for Point 1 (x y): ").split())
            )
            point2 = tuple(
                map(float, input("Enter coordinates for Point 2 (x y): ").split())
            )
            point3 = tuple(
                map(float, input("Enter coordinates for Point 3 (x y): ").split())
            )

            triangle = Triangle(point1, point2, point3)
            print(
                "\n".join(
                    [
                        "Your calculations are ready:",
                        "Shape: Triangle",
                        f"Type of triangle: {triangle.type_triangle()}",
                        f"Perimeter: {triangle.perimeter()}",
                        f"Area: {triangle.area()}",
                    ]
                )
            )
        else:
            print("This shape is not supported in our program! Please try again.")
            continue


if __name__ == "__main__":
    main()
