txt = input("Enter your text: ")
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']  

result = []
count = 0 

for i in range(len(txt)):
    count += 1
    if count == 3 and txt[i].lower() not in vowels:
        result.append(txt[i])
        result.append('_')
        count = 0  
    else:
        result.append(txt[i])
    
    if i == len(txt) - 1:
        break

modified_txt = ''.join(result)
print(modified_txt)
