Devision = lambda Num: (Num % 3 == 0) and (Num % 5 == 0)

def main():

    Data = [10, 15, 33, 45, 60, 22, 35, 90, 100, 150]

    print("List of Accepted Numbers >>>>", Data)

    FData = list(filter(Devision, Data))

    print("Numbers divisible by 3 and 5 >>>>", FData)

if __name__ == "__main__":  
    main()