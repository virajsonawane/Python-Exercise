from functools import reduce

# Product = lambda num1, num2: (num1 * num2)    #Lambda function stored in variable

def main():

    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("List of Accepted Numbers >>>>", Data)

    RData = reduce(lambda num1, num2: (num1 * num2), Data)      #Inline lambda function

    print("Product of all numbers >>>>", RData)

if __name__ == "__main__":  
    main()