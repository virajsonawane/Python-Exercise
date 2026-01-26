# Assignment 17 - Question 8

def Pattern(Number):
    for i in range(1, Number + 1):

        for j in range(1, i + 1):
        
            print(j, end=" ")
        
        print()


def main():

    Number = int(input("Enter number of rows & columns : "))

    Pattern(Number)

if __name__ == "__main__":
    main()