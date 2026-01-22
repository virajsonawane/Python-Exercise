def ChkGreater():
    print("Enter First Number : ")
    num1 = int(input())

    print("Enter Second Number : ")
    num2 = int(input())

    if (num1 > num2):
        print(num1, " is greater")
        
    else:
        print(num2, " is greater")

def main():
    ChkGreater()
    
if __name__ == "__main__":
    main()
