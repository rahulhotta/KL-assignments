"""
A python code for calculating area and perimeter for a few shapes
"""


class Rectangle:
    """
    A class to contain the methods of Rectangle
    """

    def __init__(self, rectangle_length, rectangle_breadth):
        self.length = rectangle_length
        self.breadth = rectangle_breadth

    def calculate_area(self):
        """Function for calculating the area of Rectangle"""

        area = self.length * self.breadth
        print(f"The area of rectangle is {area}")

    def calculate_perimeter(self):
        """Function for calculating the perimeter of Rectangle"""

        perimeter = 2 * (self.length + self.breadth)
        print(f"The perimeter of rectangle is {perimeter}")


class Square:
    """
    A class to contain the methods of Square
    """

    def __init__(self, square_length):
        self.length = square_length

    def calculate_area(self):
        """
        Function for calculating the area of Square
        """
        area = self.length * self.length
        print(f"The area of square is {area}")

    def calculate_perimeter(self):
        """
        Function for calculating the perimeter of Square
        """
        perimeter = 4 * (self.length)
        print(f"The perimeter of square is {perimeter}")


class Triangle:
    """
    A class to contain the methods of Triangle
    """

    def __init__(self, triangle_height, triangle_breadth, triangle_side1, triangle_side2, triangle_side3):
        self.height = triangle_height
        self.breadth = triangle_breadth
        self.side1 = triangle_side1
        self.side2 = triangle_side2
        self.side3 = triangle_side3

    def calculate_area(self):
        """
        Calculating the area of Triangle
        """
        area = 0.5 * self.breadth * self.height
        print(f"The area of triangle is {area}")

    def calculate_perimeter(self):
        """
        Calculating the perimeter of Triangle
        """
        perimeter = self.side1 + self.side2 + self.side3
        print(f"The perimeter of triangle is {perimeter}")


class Cirlcle:
    """
    A class to contain the methods of Cirlce
    """

    def __init__(self, cicle_radius):
        self.radius = cicle_radius

    def calculate_area(self):
        """
        Function for calculating the area of Circle
        """
        area = 3.14 * self.radius * self.radius
        print(f"The area of circle is {area}")

    def calculate_perimeter(self):
        """
        calculating the perimeter of Circle
        """
        perimeter = 2 * 3.14 * self.radius
        print(f"The perimeter of circle is {perimeter}")


while True:
    shape = input("Enter a shape or type exit to quit: ")

    if shape.lower() == "rectangle":
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        rectangle_object = Rectangle(length, breadth)
        rectangle_object.calculate_perimeter()
        rectangle_object.calculate_area()
    elif shape.lower() == "square":
        side = int(input("Enter the side of the square: "))
        square_object = Square(side)
        square_object.calculate_perimeter()
        square_object.calculate_area()
    elif shape.lower() == "triangle":
        height = int(input("Enter the height of the Triangle: "))
        breadth = int(input("Enter the breadth of the Triangle: "))
        side_1 = int(input("Enter the side 1 of the Triangle: "))
        side_2 = int(input("Enter the side 2 of the Triangle: "))
        side_3 = int(input("Enter the side 3 of the Triangle: "))
        triangle_object = Triangle(height, breadth, side_1, side_2, side_3)
        triangle_object.calculate_perimeter()
        triangle_object.calculate_area()
    elif shape.lower() == "circle":
        radius = int(input("Enter the radius of the circle: "))
        circle_object = Cirlcle(radius)
        circle_object.calculate_perimeter()
        circle_object.calculate_area()
    elif shape.lower() == "exit":
        print("Thank you")
        break
    else:
        print("Please enter a correct option")

    print("=========================================================")
