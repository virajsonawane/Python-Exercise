# Assignment 16 Question 8

def PrintStars(Number):
    for i in range(Number):
        print("*", end=" ")

def main():

    Number = int(input("Enter a number : "))

    PrintStars(Number)

if __name__ == "__main__":
    main()