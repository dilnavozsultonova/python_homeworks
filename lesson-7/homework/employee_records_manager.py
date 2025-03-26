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
