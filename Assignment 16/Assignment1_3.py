# Assignment 16 Question 3

def Add(Num1, Num2):
    return Num1 + Num2

def main():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))

    result = Add(number1, number2)

    print("Addition of two numbers is:", result)

if __name__ == "__main__":
    main()