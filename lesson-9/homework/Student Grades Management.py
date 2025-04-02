import csv


l=[]

with open ("lesson-9/homework/grades.csv","r") as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)
    for i in csv_reader:
        d={}
        for k in range(len(i)):
            d[header[k]]=i[k]
        l.append(d)


sum={}
counter={}

for d in l:
    if d["Subject"] in sum.keys():
        sum[d["Subject"]]+=int(d["Grade"])
        counter += 1
    else:
        sum[d["Subject"]]=int(d["Grade"])
        counter[i["Subject"]]= 1

for i in sum.keys():
    sum[i]/=counter[i]

with open("lesson-9/homework/grades.csv","w") as file:
    csv_writer=csv.writer(file)
    csv_writer=csv.writerow(["Subject","Average grade"])
    for i,j in sum.items():
        csv_writer.writerow([i,j])

