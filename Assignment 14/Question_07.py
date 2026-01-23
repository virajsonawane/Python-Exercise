Divisibleby5 = lambda n: "True" if (n % 5 == 0) else "False"

def main():

    num = int(input("Enter a Number : "))

    print(Divisibleby5(num))

if __name__ == "__main__":
    main()