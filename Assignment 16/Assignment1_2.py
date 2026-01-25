# Assignment 16 Question 2

def ChkNum(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    
    number = int(input("Enter a number : "))

    result = ChkNum(number)
    
    print(result)

if __name__ == "__main__":
    main()