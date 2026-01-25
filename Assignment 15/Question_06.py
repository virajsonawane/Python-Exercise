from functools import reduce

Addition = lambda num1, num2: min(num1, num2)

def main():

    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("List of Accepted Numbers >>>>", Data)

    RData = (reduce(Addition, Data))

    print("Maximum of all numbers >>>>", RData)

if __name__ == "__main__":  
    main()