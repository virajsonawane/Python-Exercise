from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Square(No):
    return No * No

def Add(No1, No2):
    return No1 + No2


def main():
    Data = []

    Number = int(input("Enter number of elements : "))

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    FilterData = list(filter(CheckEven, Data))
    print("List after filter :", FilterData)

    MapData = list(map(Square, FilterData))
    print("List after map :", MapData)

    Result = reduce(Add, MapData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()
