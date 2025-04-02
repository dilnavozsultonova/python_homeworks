import json
import csv

with open("lesson-9/homework/tasks.json", "r") as file:
    data = json.load(file)

total_tasks = len(data)
completed_tasks = 0
pending_tasks = 0
avg_priority = 0

for i in data:
    completed_tasks += i["completed"]
    pending_tasks += 1 - i["completed"]
    avg_priority += i["priority"]

avg_priority /= total_tasks

print(total_tasks)
print(completed_tasks)
print(pending_tasks)
print(avg_priority)

with open("lesson-9/homework/tasks.csv", "w") as file:
    csv_writer = csv.writer(file)
    header = data[0].keys()
    csv_writer.writerow(header)
    for row in data:
        csv_writer.writerow(row.values())

