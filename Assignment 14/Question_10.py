LargestNum = lambda n1, n2, n3: n1 if (n1 >= n2 and n1 >= n3) else (n2 if (n2 >= n1 and n2 >= n3) else n3)
# we also use max built-in function to find largest number =  eg. max(n1, n2, n3)

def main():

    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    num3 = int(input("Enter Third Number : "))

    print("The Largest Number is >>>>", LargestNum(num1, num2, num3))

if __name__ == "__main__":  
    main()