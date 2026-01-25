# Assignment 17 - Question 1

import Arithmetic

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", Arithmetic.Add(num1, num2))
    print("Subtraction:", Arithmetic.Sub(num1, num2))
    print("Multiplication:", Arithmetic.Mul(num1, num2))
    print("Division:", Arithmetic.Div(num1, num2))

if __name__ == "__main__":
    main()