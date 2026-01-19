def main():
    print("Enter a Number : ")
    num = int(input())
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

    print("Count of Given Number is :",count)

if __name__ == "__main__":
    main()