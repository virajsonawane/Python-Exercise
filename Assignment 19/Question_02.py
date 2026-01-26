def main():
    Multiply = lambda No1, No2: No1 * No2

    Number1 = int(input("Enter first number : "))
    Number2 = int(input("Enter second number : "))

    Result = Multiply(Number1, Number2)

    print("Result is :", Result)


if __name__ == "__main__":
    main()
