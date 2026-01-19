def main():
    print("Enter a Number : ")
    num = int(input())
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    print("Sum of Given Number is :", total)

if __name__ == "__main__":
    main()