def BinaryNum(Num):

    Binary = ""

    while Num > 0:
        Remainder = Num % 2
        Binary = str(Remainder) + Binary
        Num = Num // 2
    
    print("Binary of the number is : ", Binary)

def main():

    Bin = int(input("Enter a Number : "))

    BinaryNum(Bin)

if __name__ == "__main__":
    main()