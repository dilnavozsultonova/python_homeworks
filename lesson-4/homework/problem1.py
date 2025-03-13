a = list(map(int,input().split()))
b = list(map(int,input().split()))
uncommon_a=(x for x in a if x not in b)
uncommon_b=(x for x in b if x not in a)

for element in uncommon_a:
    print(element)

for element in uncommon_b:
    print(element)
        

    
