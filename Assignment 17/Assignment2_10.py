# Assignment 17 - Question 10

def SumDigit(num):
    total = 0

    while num > 0:

        digit = num % 10

        total += digit

        num = num // 10
    
    print("Sum of digits:", total)
    
def main():

    Number = int(input("Enter a number: "))
    SumDigit(Number)


if __name__ == "__main__":
    main()