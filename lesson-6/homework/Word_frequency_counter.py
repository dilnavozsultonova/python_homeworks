from pathlib import Path

cur_dir = Path(__file__).resolve().parent

try:
    with open(cur_dir / "sample.txt","r"):
        pass
except:
    with open(cur_dir / "sample.txt","w") as file:
        etc=input("Enter your paragraph: ")
        file.write(etc)
file=open(cur_dir / "sample.txt","r")

cnt = dict()

for line in file.readlines():
    s = ""
    for i in line:
        if i.isalpha():
            s += i.lower()
        else:
            if s!="":
                if s in cnt.keys():
                    cnt[s] += 1
                else:
                    cnt[s] = 1
            s = ""

    if s!="":
        if s in cnt.keys():
            cnt[s] += 1
        else:
            cnt[s] = 1

l = []
total = 0

for key, value in cnt.items():
    l.append([value,key])
    total += value

l.sort(reverse=True)



file=open(cur_dir / "word_count_report.txt","w")
file.write(f"Word Count Report\nTotal words: {total}\n")
for i in range(min(len(l),5)):
    file.write(f"{l[i][1]} - {l[i][0]}\n")



num=int(input("Enter the number : "))
for i in range(min(len(l),num)):
    print(f"{l[i][1]} - {l[i][0]}\n")