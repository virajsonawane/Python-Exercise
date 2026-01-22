Cube = lambda num1: num1 ** 3

def main():
    
    num = int(input("Enter a number: "))
    
    print("The cube of", num, "is", Cube(num))

if __name__ == "__main__":
    main()