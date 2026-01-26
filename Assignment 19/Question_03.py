from functools import reduce

def CheckNumber(No):
    return (No >= 70 and No <= 90)

def Increase(No):
    return No + 10

def Multiply(No1, No2):
    return No1 * No2


def main():
    Data = []

    Number = int(input("Enter number of elements : "))

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    FilterData = list(filter(CheckNumber, Data))
    print("List after filter :", FilterData)

    MapData = list(map(Increase, FilterData))
    print("List after map :", MapData)

    Result = reduce(Multiply, MapData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()
