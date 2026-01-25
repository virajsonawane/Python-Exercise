length = lambda Str: len(Str) > 5

def main():

    Data = ["Viraj", "Sanket", "Akash", "Ankush", "Prathamesh", "Amol", "Shubham"]

    print("List of Accepted Strings >>>>", Data)

    FData = list(filter(length, Data))

    print("Strings with length greater than 5 >>>>", FData)

if __name__ == "__main__":  
    main()