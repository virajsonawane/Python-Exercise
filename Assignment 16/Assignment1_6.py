# Assignment 16 Question 6

def PositiveNegative(num):
    
    if num == 0:
        print("Zero")
    
    elif num > 0:
        print("Positive number")
    
    elif num < 0:
        print("Negative number")

def main():
    
    num = int(input("Enter a number : "))
    
    PositiveNegative(num)

if __name__ == "__main__":
    main()