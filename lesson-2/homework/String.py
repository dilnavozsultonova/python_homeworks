# # 1. Create a program to ask name and year of birth from user and tell them their age.
name=input("Your name:")
year=int(input("Year of birth:"))
print(2025-year)




# # 2. Extract car names from this text:
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])




# # 3. Write a Python program to:
# #    - Take a string input from the user.
# #    - Print the length of the string.
# #    - Convert the string to uppercase and lowercase.
str=input("word:")
print(len(str))
print(str.upper())
print(str.lower())





# # 4. Write a Python program to check if a given string is `palindrome` or not.
pl=input("Word:")
if pl==pl[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")


# # > What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

# # 5. Write a program that counts the number of vowels and consonants in a given string.
txt=input()
vowels=['a','o','u','e','i']
c=0
t=0
for i in range(len(txt)):
    if txt[i].lower() in vowels:
        c += 1
    else:
        t +=1
print("Number of vowels: ",c)
print("Number of consonants: ",t)



# # 6. Write a Python program to check if one string contains another.
s=input()
t=input()
if t in s:
    print("Yes")
else:
    print("No")    


# # 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."
sentence=input("Sentence:")
word=input("word:")
another_word=input("Another word:")
sentence=sentence.replace(word,another_word)
print("new sentence",sentence)


# 8. Write a program that asks the user for a string and prints the first and last characters of the string.  
word=input()
print(word[0::-1])
print(word[-1])


# 9. Ask the user for a string and print the reversed version of it.
sentence=input()
print(sentence[::-1])



# 10. Write a program that asks the user for a sentence and prints the number of words in it.  
sentence=input("Sentence:")
print("Number of words:",sentence.count(" ")+1)



# 11. Write a program to check if a string contains any digits.  
s=input()
ok=False
for i in range(len(s)):
    if s[i].isdigit():
        ok=True
if(ok):
    print("yes")
else:
    print("no")



# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  

def join_words(word_list, separator):
    return separator.join(word_list)

word1=input()
word2=input()
word3=input()

words = [word1,word2,word3]
separator = ", "  
result = join_words(words, separator)

print(result) 





# 13. Ask the user for a string and remove all spaces from it.  
txt=input()
print(txt.replace(" ",""))




# 14. Write a program to ask for two strings and check if they are equal or not.  
word1=input()
word2=input()
if word1 == word2:
    print("They are equal")
else:
    print("They are not equal")
    


# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
#     Example:  
#     - Input: "World Health Organization"  
#     - Output: "WHO"  
sentence = input("Enter a sentence: ")
words = sentence.split()
acronym = ''.join([word[0].upper() for word in words])
print("The acronym is:", acronym)




# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
word=input("String:")
character=input("character:")
word=word.replace(character,"")
print(word)




# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
txt = input("Enter a string: ")
vowels = ['a', 'o', 'u', 'e', 'i']

for i in range(len(txt)):
    if txt[i].lower() in vowels:
        txt = txt[:i] + "*" + txt[i+1:]

print(txt)







# 18. Write a program that checks if a string starts with one word and ends with another.  
#     Example:  
#     - Input: "Python is fun!"  
#     - Starts with: "Python"  
#     - Ends with: "fun!"  
input_string = input("Enter a string: ")

start_word = input("Enter the word that the string should start with: ")
end_word = input("Enter the word that the string should end with: ")


if input_string.startswith(start_word) and input_string.endswith(end_word):
    print(f"The string starts with '{start_word}' and ends with '{end_word}'.")
else:
    print(f"The string does not start with '{start_word}' and end with '{end_word}'.")
