import json
import csv
from datetime import datetime


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        due_str = self.due_date if self.due_date else "N/A"
        return f"{self.task_id}, {self.title}, {self.description}, {due_str}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }


class FileStorage:
    def __init__(self, filename, file_format="json"):
        self.filename = filename
        self.file_format = file_format

    def save(self, tasks):
        if self.file_format == "json":
            self.save_json(tasks)
        elif self.file_format == "csv":
            self.save_csv(tasks)

    def load(self):
        if self.file_format == "json":
            return self.load_json()
        elif self.file_format == "csv":
            return self.load_csv()

    def save_json(self, tasks):
        try:
            with open(self.filename, 'w') as file:
                json.dump([task.to_dict() for task in tasks], file, default=str, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_json(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return []

    def save_csv(self, tasks):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["task_id", "title", "description", "due_date", "status"])
                for task in tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_csv(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(
                        task_id=row['task_id'],
                        title=row['title'],
                        description=row['description'],
                        due_date=row['due_date'] if row['due_date'] != 'N/A' else None,
                        status=row['status']
                    )
                    tasks.append(task)
        except (FileNotFoundError, csv.Error) as e:
            print(f"Error reading file: {e}")
        return tasks

class TaskManager:
    def __init__(self, storage: FileStorage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        if not any(t.task_id == task.task_id for t in self.tasks):
            self.tasks.append(task)
            self.storage.save(self.tasks)
            print("Task added successfully!")
        else:
            print(f"Error: Task with ID {task.task_id} already exists.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if task:
            if title: task.title = title
            if description: task.description = description
            if due_date: task.due_date = due_date
            if status: task.status = status
            self.storage.save(self.tasks)
            print(f"Task {task_id} updated successfully!")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if task:
            self.tasks.remove(task)
            self.storage.save(self.tasks)
            print(f"Task {task_id} deleted successfully!")
        else:
            print(f"Task with ID {task_id} not found.")

    def filter_tasks(self, status):
        filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
        if filtered:
            print(f"Tasks with status {status}:")
            for task in filtered:
                print(task)
        else:
            print(f"No tasks found with status {status}.")

def main():
    print("Welcome to the To-Do Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Filter tasks by status")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

   
    file_format = input("Enter file format (json/csv): ").strip().lower()
    storage = FileStorage("tasks." + file_format, file_format)
    task_manager = TaskManager(storage)

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ")
            due_date = due_date if due_date else None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, due_date, status)
            task_manager.add_task(task)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep current): ")
            description = input("Enter new Description (leave blank to keep current): ")
            due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to keep current): ")
            status = input("Enter new Status (Pending/In Progress/Completed, leave blank to keep current): ")
            task_manager.update_task(task_id, title, description, due_date or None, status or None)

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            task_manager.delete_task(task_id)

        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ")
            task_manager.filter_tasks(status)

        elif choice == "6":
            task_manager.storage.save(task_manager.tasks)
            print("Tasks saved successfully.")

        elif choice == "7":
            task_manager.tasks = task_manager.storage.load()
            print("Tasks loaded successfully.")

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
