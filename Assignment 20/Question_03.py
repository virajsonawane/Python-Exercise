import threading

def EvenList(Data):
    Sum = 0
    EvenNumbers = []

    for i in Data:
        if i % 2 == 0:
            EvenNumbers.append(i)
            Sum = Sum + i

    print("Even elements are :", EvenNumbers)
    print("Sum of even elements :", Sum)


def OddList(Data):
    Sum = 0
    OddNumbers = []

    for i in Data:
        if i % 2 != 0:
            OddNumbers.append(i)
            Sum = Sum + i

    print("Odd elements are  :", OddNumbers)
    print("Sum of odd elements  :", Sum)


def main():
    Data = []
    n = int(input("Enter number of elements : "))

    for i in range(n):
        value = int(input("Enter element : "))
        Data.append(value)

    t1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
