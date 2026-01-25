# Assignment 17 - Question 3

def Factorial(num):
    fact = 1

    for i in range(1, num + 1):

        fact = fact * i
    
    return fact

def main():
    number = int(input("Enter a number : "))

    result = Factorial(number)
    
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()