def main():

    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("List of Accepted Numbers >>>>", Data)

    RData = list(filter(lambda x: x % 2 == 0, Data))

    print("Count of Even numbers >>>>", len(RData))

if __name__ == "__main__":  
    main()