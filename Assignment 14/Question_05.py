Even = lambda n: "Even" if (n % 2 == 0) else "Odd"

def main():

    num = int(input("Enter a Number : "))

    print("The number is >>>>", Even(num))

if __name__ == "__main__":
    main()