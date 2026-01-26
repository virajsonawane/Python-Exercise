# Assignment 17 - Question 5

def PrimeCheck(num):

    count = 0

    for i in range(1, num + 1):

        if num % i == 0:
            
            count = count + 1

    if count == 2:
        
        print("It is a Prime number")
    
    else:
        
        print("It is Not prime number")

def main():

    num = int(input("Enter a number: "))

    PrimeCheck(num)

if __name__ == "__main__":
    main()