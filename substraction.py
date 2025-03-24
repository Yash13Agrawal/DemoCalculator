# DemoCalculator
class Calculator:
    @staticmethod
    def subtract(a, b):
        return a - b
# Sample input
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Subtraction:", Calculator.subtract(num1, num2))
