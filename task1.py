mylist=input("Enter the list members:").split()


def is_palindrome(mylist):
   for word in mylist:
    if word==word[::-1]:
        return True
    else:
        return False
    
print(is_palindrome(mylist))