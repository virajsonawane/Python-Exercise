def main():
    print("Enter a Number : ")
    num = int(input())
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    print("Reverse of Given Number is :", reverse)

if __name__ == "__main__":
    main()