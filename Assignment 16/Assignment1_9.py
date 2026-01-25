# Assignment 16 Question 9

def TenEvenNumbers():
    count = 0
    Number = 1

    while count < 10:

        if Number % 2 == 0:

            print(Number, end=" ")

            count += 1
            
        Number += 1

def main():

    TenEvenNumbers()

if __name__ == "__main__":
    main()