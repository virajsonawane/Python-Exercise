def Factor(N):
    for i in range(N, 0, -1):
            print(i)


def main():
    print("Enter a Number : ")
    num = int(input())
    Factor(num)

if __name__ == "__main__":
    main()