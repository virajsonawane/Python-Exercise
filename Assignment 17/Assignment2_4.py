# Assignment 17 - Question 4

def SumOfFactors(number):
    total = 0
    
    for i in range(1, number):   
        
        if number % i == 0:      
            
            total += i           
    
    return total

def main():
    
    num = int(input("Enter a number: "))

    sum = SumOfFactors(num)

    print(f"The sum of factors of {num} is {sum}")

if __name__ == "__main__":
    main() 