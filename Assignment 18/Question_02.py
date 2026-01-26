def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    return Max


def main():
    Number = int(input("Enter number of elements : "))
    Data = []

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    Result = Maximum(Data)

    print("Maximum number is :", Result)


if __name__ == "__main__":
    main()
