# Assignment 16 Question 10

def length(str):
    count = 0
    for i in str:
        count += 1
    print(count)

def main():
    
    str = input("Enter a string: ")
    length(str)

if __name__ == "__main__":
    main()