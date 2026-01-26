import threading

def MaxThread(Data):
    Max = Data[0]
    for i in Data:
        if i > Max:
            Max = i
    print("Maximum element is :", Max)


def MinThread(Data):
    Min = Data[0]
    for i in Data:
        if i < Min:
            Min = i
    print("Minimum element is :", Min)


def main():
    Data = []
    n = int(input("Enter number of elements : "))

    for i in range(n):
        value = int(input("Enter element : "))
        Data.append(value)

    t1 = threading.Thread(target=MaxThread, args=(Data,), name="MaxThread")
    t2 = threading.Thread(target=MinThread, args=(Data,), name="MinThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
