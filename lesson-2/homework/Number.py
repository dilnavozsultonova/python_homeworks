# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.
n=float(input())
print(f"{n:.2f}")




# 2. Write a Python file that asks for three numbers and outputs the largest and smallest.
import math
n=float(input("first number is "))
n2=float(input("second number is "))
n3=float(input("third number is "))
print(max(n,n2,n3))
print(min(n,n2,n3))



# 3. Create a program that converts kilometers to meters and centimeters.
c=int(input("Kilometers:"))
meters=c*1000
centimeters=meters*100
print(meters)
print(centimeters)



# 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
num1=int(input("First:"))
num2=int(input("Second:"))
print(num1//num2)
print(num1%num2)




# 5. Make a program that converts a given Celsius temperature to Fahrenheit.
l=int(input("Celsius:"))
Fahrenheit=l+273
print(Fahrenheit)



# 6. Create a program that accepts a number and returns the last digit of that number.
n=(input("Number:"))
print(n[-1])



# 7. Create a program that takes a number and checks if it’s even or not.
n=int(input("Number:"))
if n%2==0:
    print("It is even")
else:
    print("It is odd")

