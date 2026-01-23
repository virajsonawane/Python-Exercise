Odd = lambda n: "True" if (n % 2 != 0) else "False"

def main():

    num = int(input("Enter a Number : "))

    print( Odd(num))

if __name__ == "__main__":
    main()