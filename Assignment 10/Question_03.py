def main():
    print("Enter Number : ")
    num = int(input())
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is", fact)

if __name__ == "__main__":
    main()