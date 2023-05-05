# Making an calculator using class and objects
class Calculator:
    def __init__(self, number_1,number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    def addition(self):
        return self.number_1 + self.number_2
    
    def subtraction(self):
        return self.number_1 - self.number_2
    
    def multiplication(self):
        return self.number_1 * self.number_2
    
    def division(self):
        return self.number_1 / self.number_2


def take_user_input(): 
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    numbers = Calculator(number1, number2)
    return numbers

while True :
    operation = int(input(" Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n Enter 5 for exit \n"))

    if operation == 1:
        numbers = take_user_input()
        print("The addition of the numbers is",numbers.addition())
    elif operation == 2:
        numbers = take_user_input()
        print("The subtraction of the numbers is",numbers.subtraction())
    elif operation == 3:
        numbers = take_user_input()
        print("The multiplication of the numbers is",numbers.multiplication())
    elif operation == 4:
        numbers = take_user_input()
        print("The division of the numbers is",numbers.division())
    elif operation == 5:
        print("Thank you")
        break
    else:
        print("Please enter a correct option")

    print("=========================================================")
