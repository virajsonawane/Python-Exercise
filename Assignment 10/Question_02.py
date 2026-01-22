def main():
    print("Enter Number : ")
    num = int(input())
    sum = 0

    for i in range(1, num + 1):
        sum += i

    print("Sum of Frist", num, "Natural Number is", sum)

if __name__ == "__main__":
    main()