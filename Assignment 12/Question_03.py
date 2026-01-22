def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a, b):
    return a / b

def main():

    print("Enter First Number : ")
    num1 = int(input())
    print("Enter Second Number : ")
    num2 = int(input())

    print("Addition : ", Addition(num1, num2))
    print("Subtraction : ", Subtraction(num1, num2))
    print("Multiplication : ", Multiplication(num1, num2))
    print("Division : ", Division(num1, num2))

if __name__ == "__main__":
    main()