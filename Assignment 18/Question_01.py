def AddListElements(Data):
    Sum = 0

    for i in Data:
        Sum = Sum + i

    return Sum


def main():
    Number = int(input("Enter number of elements : "))
    Data = []

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    Result = AddListElements(Data)

    print("Addition of all elements is :", Result)


if __name__ == "__main__":
    main()
