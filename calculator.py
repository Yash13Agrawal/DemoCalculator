class Calculator:
 @staticmethod
 def divide(a, b):
  if b == 0:
    return "Error: Division by zero is not allowed."
  return a / b
        
             # Sample input
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Division:", Calculator.divide(num1, num2))
