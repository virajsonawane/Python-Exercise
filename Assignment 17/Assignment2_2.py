# Assignment 17 - Question 2

def Pattern(Number):
    for i in range(Number):

        for j in range(Number):

            print("*", end=" ")
            
        print()


def main():

    Number = int(input("Enter number of rows & columns : "))

    Pattern(Number)

if __name__ == "__main__":
    main()