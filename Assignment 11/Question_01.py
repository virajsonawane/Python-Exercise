def main():
    print("Enter a Number : ")
    num = int(input())
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print("Prime number")
    else:
        print("Not prime number")

if __name__ == "__main__":
    main()