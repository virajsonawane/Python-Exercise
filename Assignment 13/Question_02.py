def AreaCircle(Red):
    
    Area = 3.14 * Red * Red

    print("Area of Circle is : ", Area)


def main():

    Red = int(input("Enter the Redius of the circle : "))

    AreaCircle(Red)

if __name__ == "__main__":
    main()