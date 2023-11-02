import math


def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)


def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius


def calculate_circle_area(radius):
    return math.pi * (radius**2)


def calculate_triangle_perimeter(side_1, side_2, side_3):
    return side_1 + side_2 + side_3


def calculate_triangle_area(side_1, side_2, side_3):
    half_perimeter = calculate_triangle_perimeter(side_1, side_2, side_3) / 2
    return math.sqrt(
        half_perimeter
        * (half_perimeter - side_1)
        * (half_perimeter - side_2)
        * (half_perimeter - side_3)
    )


def type_triangle(side_1, side_2, side_3):
    if (
        (side_1 + side_2 > side_3)
        and (side_1 + side_3 > side_2)
        and (side_2 + side_3 > side_1)
    ):
        if side_1 == side_2 == side_3:
            return "equilateral"
        elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "Triangle doesn't exist! Input another sides."


def main():
    while True:
        shape_type = input("Write shape type for calculations or 'quit' to exit: ")
        if shape_type == "quit":
            break
        elif shape_type == "triangle":
            side_1 = abs(float(input("Enter side 1 of your triangle: ")))
            side_2 = abs(float(input("Enter side 2 of your triangle: ")))
            side_3 = abs(float(input("Enter side 3 of your triangle: ")))
            type_tria = type_triangle(side_1, side_2, side_3)
            per = calculate_triangle_perimeter(side_1, side_2, side_3)
            area = calculate_triangle_area(side_1, side_2, side_3)
            print(
                f"Shape: {shape_type}, Type of triangle: {type_tria}, Perimeter: {per}, Area: {area}"
            )
        elif shape_type == "circle":
            radius = abs(float(input("Enter the radius: ")))
            per = calculate_circle_perimeter(radius)
            area = calculate_circle_area(radius)
            print(f"Shape: {shape_type}, Perimeter: {per}, Area: {area}")
        elif shape_type == "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            per = calculate_rectangle_perimeter(length, width)
            area = calculate_rectangle_area(length, width)
            print(f"Shape: {shape_type}, Perimeter: {per}, Area: {area}")
        else:
            print("This shape is not supported in our program! Please try again!")
            continue


if __name__ == "__main__":
    main()
