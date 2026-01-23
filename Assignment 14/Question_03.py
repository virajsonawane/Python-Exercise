Max = lambda n1, n2: n1 if (n1 > n2) else n2

def main():

    num1 = int(input("Enter first Number : "))

    num2 = int(input("Enter second Number : "))

    print("Maximum Number is : ", Max(num1, num2))

if __name__ == "__main__":
    main()