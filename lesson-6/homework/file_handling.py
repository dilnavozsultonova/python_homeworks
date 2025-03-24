def add_employee():
    with open("employee.txt","a") as file:
        print("Enter the employee details")

        employee_id=input("Employee ID: ")
        name= input("Name: ")
        position = input("Position: ")
        salary=input("Salary: ")

        record=f"{employee_id},{name},{salary}\n"

        file.write(record)
        print("Employee record added successfully")
