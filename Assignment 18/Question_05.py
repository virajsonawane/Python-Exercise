import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for i in Data:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum


def main():
    Number = int(input("Enter number of elements : "))
    Data = []

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    Result = ListPrime(Data)

    print("Addition of all prime numbers is :", Result)


if __name__ == "__main__":
    main()
