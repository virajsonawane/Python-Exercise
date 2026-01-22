def Area(length, width):
    
    Cal = length * width

    print("The area of the rectangle is: ", Cal)

def main():
    
    len = int(input("Enter the length of the rectangle: "))

    wid = int(input("Enter the width of the rectangle: "))

    Area(len, wid)

if __name__ == "__main__":
    main()