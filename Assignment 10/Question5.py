def main():

    print("Enter a Number : ")
    num = int(input())

    print("Odd Numbers are : ")

    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)

if __name__ == "__main__":
    main()