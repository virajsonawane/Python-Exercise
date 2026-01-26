def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    return Min


def main():
    Number = int(input("Enter number of elements : "))
    Data = []

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    Result = Minimum(Data)

    print("Minimum number is :", Result)


if __name__ == "__main__":
    main()
