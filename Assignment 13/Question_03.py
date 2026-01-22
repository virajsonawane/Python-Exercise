def PerfectNum(Num):
    
    Sum = 0
    
    for i in range(1, Num):
        if (Num % i == 0):
            Sum += i

    if (Sum == Num):
        print("Perfect Number.")
    else:
        print("Not a Perfect Number.")

def main():

    Perfect = int(input("Enter a Number : "))

    PerfectNum(Perfect)

if __name__ == "__main__":
    main()