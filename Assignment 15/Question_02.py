Even = lambda num: (num % 2 == 0)

def main():

    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("List of Accepted Numbers >>>>", Data)

    FData = list(filter(Even, Data))

    print("List of Even Numbers using filter >>>>", list(FData))

if __name__ == "__main__":  
    main()