import math

def isPrime():
    number = int(input("Enter a number: "))
    
    if number < 2:
        print("It is not a prime number")
        return
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print("It is not a prime number")
            return
    
    print("It is a prime number")

isPrime()

