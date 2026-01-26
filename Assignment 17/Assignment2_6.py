# Assignment 17 - Question 6

def Pattern(Number):
    for i in range(Number, 0, - 1):

        for j in range(i):
        
            print("*", end=" ")
        
        print()


def main():

    Number = int(input("Enter number of rows & columns : "))

    Pattern(Number)

if __name__ == "__main__":
    main()