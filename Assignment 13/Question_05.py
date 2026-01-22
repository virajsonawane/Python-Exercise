def Grade(Score):
    if Score >= 75:
        print("Distinction")
    elif Score >= 60:
        print("First Class")
    elif Score >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    
    Mark = int(input("Enter Your Mark : "))

    Grade(Mark)

if __name__ == "__main__":
    main()