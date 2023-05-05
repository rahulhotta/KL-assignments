"""
A python code for calculating area and perimeter for a few shapes
"""

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        area = self.length * self.breadth
        print(f"The area of rectangle is {area}.")
    def calculate_perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        print(f"The perimeter of rectangle is {perimeter}.")

class Square:
    def __init__(self, length):
        self.length = length
    def calculate_area(self):
        area = self.length * self.length
        print(f"The area of square is {area}.")
    def calculate_perimeter(self):
        perimeter = 4*(self.length)
        print(f"The perimeter of square is {perimeter}.")


class Triangle:
    def __init__(self, height, breadth, side1, side2, side3):
        self.height = height
        self.breadth = breadth
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        area = 0.5 * self.breadth * self.height
        print(f"The area of triangle is {area}.")
    def calculate_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print(f"The perimeter of triangle is {perimeter}.")


class Cirlcle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area = 3.14* self.radius * self.radius
        print(f"The area of circle is {area}.")
    def calculate_perimeter(self):
        perimeter = 2*3.14*self.radius
        print(f"The perimeter of circle is {perimeter}.")



while True :
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
        triangle_object = Triangle(height,breadth,side_1,side_2,side_3)
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



