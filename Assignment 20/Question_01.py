import threading

def Even():
    count = 0
    number = 2

    while count < 10:
        print("Even :", number)
        number = number + 2
        count = count + 1


def Odd():
    count = 0
    number = 1

    while count < 10:
        print("Odd  :", number)
        number = number + 2
        count = count + 1


def main():
    t1 = threading.Thread(target=Even, name="Even")
    t2 = threading.Thread(target=Odd, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
