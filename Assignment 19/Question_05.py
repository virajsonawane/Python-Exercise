from functools import reduce

def CheckPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def MultiplyByTwo(No):
    return No * 2


def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2


def main():
    Data = []

    Number = int(input("Enter number of elements : "))

    for i in range(Number):
        value = int(input("Enter element : "))
        Data.append(value)

    FilterData = list(filter(CheckPrime, Data))
    print("List after filter :", FilterData)

    MapData = list(map(MultiplyByTwo, FilterData))
    print("List after map :", MapData)

    Result = reduce(Maximum, MapData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()
