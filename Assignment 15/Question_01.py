Square = lambda num: num * num

def main():

    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("List of Accepted Numbers >>>>", Data)

    MData = list(map(Square, Data))

    print("List of Square Numbers using map >>>>", list(MData))
    
if __name__ == "__main__":  
    main()