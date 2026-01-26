import threading

def Prime(Data):
    Primes = []
    for No in Data:
        if No > 1:
            flag = True
            for i in range(2, No):
                if No % i == 0:
                    flag = False
                    break
            if flag:
                Primes.append(No)
    print("Prime numbers are :", Primes)


def NonPrime(Data):
    NonPrimes = []
    for No in Data:
        if No <= 1:
            NonPrimes.append(No)
        else:
            flag = False
            for i in range(2, No):
                if No % i == 0:
                    flag = True
                    break
            if flag:
                NonPrimes.append(No)
    print("Non-prime numbers are :", NonPrimes)


def main():
    Data = []
    n = int(input("Enter number of elements : "))

    for i in range(n):
        value = int(input("Enter element : "))
        Data.append(value)

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
