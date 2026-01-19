def main():
    print("Enter a Number : ")
    num = int(input())
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome")   
    else:
        print("Not a Palindrome.")

if __name__ == "__main__":
    main()