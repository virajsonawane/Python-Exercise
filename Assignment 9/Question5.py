def main():
    print("Enter Number : ")
    num = int(input())

    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by 3 and 5")

    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()