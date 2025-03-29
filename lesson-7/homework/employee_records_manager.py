class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary=salary
   

class EmployeeManager:
    def __init__(self,filename="employee.txt"):
        self.filename=filename
        self.load_employees()
    def load_employees(self):
        self.employees=[]
        try:
            with open(self.filename,"r") as file:
                for line in file:
                    line=line.strip()
                    if line:
                        employee_data=line.split(",")
                        self.employees.append({"id":employee_data[0],"name":employee_data[1],"position":employee_data[2],"salary":employee_data[3]})
        except FileNotFoundError:
            pass
    def save_employees(self):
        with open(self.filename,"w") as file:
            for employee in self.employees:
                file.write(f"{employee['id']},{employee['name']},{employee['position']},{employee['salary']}\n")

    def add_employee(self,employee_id,name,position,salary):
         new_employee = {
            "id": employee_id,
            "name": name,
            "position": position,
            "salary": salary
        }
         self.employees.append(new_employee)
         self.save_employees()
         print(f"Employee {name} added successfully.")

    def view_all_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for employee in self.employees:
                print(f"Employee found: ID: {employee['id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}")
                return
            print(f"Employee with ID {id} not found.")
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Update an employee's information."""
        for employee in self.employees:
            if employee["id"] == employee_id:
                if name:
                    employee["name"] = name
                if position:
                    employee["position"] = position
                if salary is not None:
                    employee["salary"] = salary
                self.save_employees()
                print(f"Employee with ID {employee_id} updated successfully.")
                return
        print(f"Employee with ID {employee_id} not found.")
    def delete_employee(self, employee_id):
        """Delete an employee by ID."""
        for employee in self.employees:
            if employee["id"] == employee_id:
                self.employees.remove(employee)
                self.save_employees()
                print(f"Employee with ID {employee_id} deleted successfully.")
                return
        print(f"Employee with ID {employee_id} not found.")
if __name__== "__main__":
    manager = EmployeeManager()

    while True:
        print("\Employee Management system")
        print("1.Add Employee")
        print("2.View Employee")
        print("3.Update Employee")
        print("4.Delete Employee")
        print("5.Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            emp_id=input("Enter Employee ID: ")
            name=input("Enter employee name: ")
            position=input("Enter employee position: ")
            salary=float(input("Enter employee salary: "))
            emp=Employee(emp_id,name,position,salary)
            manager.add_employee(emp)
            print("Employee added successfully")
        elif choice=="2":
            manager.view_all_employees()
        elif choice == "3":
            emp_id = input("Enter employee ID to search: ")
            manager.search_employee_by_id(emp_id)
        elif choice=="4":
              emp_id = input("Enter employee ID to update: ")
              name = input("Enter new name (leave blank to keep current): ")
              position = input("Enter new position (leave blank to keep current): ")
              salary = input("Enter new salary (leave blank to keep current): ")
              salary = float(salary) if salary else None
              manager.update_employee(emp_id, name, position, salary)
        elif choice=="5":
            emp_id=input("Enter employee ID: ")
            manager.delete_employee(emp_id)
        elif choice=="6":
            print("Goodbye")
            break
        else:
            print("Invalid choice.Try again:")

