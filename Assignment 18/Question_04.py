def Frequency(Data, No):
    Count = 0

    for i in Data:
        if i == No:
            Count = Count + 1

    return Count


def main():
    Number = int(input("Enter number of elements : "))
    Data = []

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    Search = int(input("Enter element to search : "))

    Result = Frequency(Data, Search)

    print("Frequency of number is :", Result)


if __name__ == "__main__":
    main()
