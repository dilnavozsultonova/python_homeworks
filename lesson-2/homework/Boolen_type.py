# 1. Write a program that accepts a username and password and checks if both are not empty.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username and password:
    print("Both username and password are entered.")
else:
    print("Username and/or password cannot be empty.")





# 2. Create a program that checks if two numbers are equal and outputs a message if they are.
num1=int(input())
num2=int(input())
if num1 == num2:
    print("They are equal")
else:
    print("They are not equal")




# 3. Write a program that checks if a number is positive and even.
num=int(input())
if num>0 and num%2==0:
    print("It is even and positive")
else:
    print("It is not even and positive")



# 4. Write a program that takes three numbers and checks if all of them are different.
num1=int(input())
num2=int(input())
num3=int(input())
if num1!=num2 and num2!=num3 and num1 != num3:
    print("They are different")
else:
    print("They are not different")




# 5. Create a program that accepts two strings and checks if they have the same length.
word1=input()
word2=input()
k=len(word1)
t=len(word2)
if k==t:
    print("They have the same length")
else:
    print("They have different lengths")




# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
number=int(input())
if number%3==0 and number%5==0:
    print("It is divisible by both 3 and 5")
else:
    print("It is not divisible by both 3 and 5")




# 7. Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)
numb=float(input())
numb1=float(input())
if numb+numb1>50.8:
   print("The sum of the two numbers is greater than 50.8")
else:
   print("The sum of the two numbers is not greater than 50.8")



num = float(input("Enter a number: "))
if 10 <= num <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")
  