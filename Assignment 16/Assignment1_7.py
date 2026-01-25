# Assignment 16 Question 7

def DevideByFive(Num):
    if Num % 5 == 0:
        return print("True")
    else:
        return print("False")

def main():

    Number = int(input("Enter a number : "))

    DevideByFive(Number)

if __name__ == "__main__":
    main()