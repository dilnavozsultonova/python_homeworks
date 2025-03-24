def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("All Employee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")
    except FileNotFoundError:
        print("Employee file not found. Please add records first.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            for record in records:
                if record.startswith(emp_id):
                    print(f"Employee Record Found: {record.strip()}")
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("Employee file not found. Please add records first.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False
    lines = []
    
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        
        with open("employees.txt", "w") as file:
            for line in lines:
                if line.startswith(emp_id):
                    print(f"Current record: {line.strip()}")
                    name = input("New Name: ")
                    position = input("New Position: ")
                    salary = input("New Salary: ")
                    updated_record = f"{emp_id}, {name}, {position}, {salary}\n"
                    file.write(updated_record)  # Write updated record
                    print("Employee record updated successfully.")
                    found = True
                else:
                    file.write(line)  # Write unchanged records
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("Employee file not found. Please add records first.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False
    lines = []
    
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
        
        with open("employees.txt", "w") as file:
            for line in lines:
                if line.startswith(emp_id):
                    print(f"Deleted record: {line.strip()}")
                    found = True
                else:
                    file.write(line)  # Write unchanged records
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("Employee file not found. Please add records first.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
