# Assignment 17 - Question 9

def DigitCount(num):
    count = 0

    while num > 0:

        num = num // 10

        count += 1
    
    print("Number of digits:", count)

def main():

    Number = int(input("Enter a number: "))
    DigitCount(Number)


if __name__ == "__main__":
    main()