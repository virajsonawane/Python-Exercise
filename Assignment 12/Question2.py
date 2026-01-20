def main():

    print("Enter a Number : ")
    num = int(input())
    
    for i in range(1, num + 1):
        if (num % i == 0):
            print(i)

if __name__ == "__main__":
    main()