import threading

def EvenFactor(No):
    Sum = 0
    print("Even factors of", No, "are:", end=" ")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i, end=" ")
            Sum = Sum + i
    print("\nSum of even factors:", Sum)


def OddFactor(No):
    Sum = 0
    print("Odd factors of", No, "are:", end=" ")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i, end=" ")
            Sum = Sum + i
    print("\nSum of odd factors:", Sum)


def main():
    Number = int(input("Enter a number : "))

    t1 = threading.Thread(target=EvenFactor, args=(Number,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(Number,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
