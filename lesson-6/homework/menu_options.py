file=open("employee.txt","w+")
while(True):
    print("1.Add new employee record")
    print("2.View all employee records")
    print("3.Search for an employee by Employee ID")
    print("4.Update an employee's information")
    print("5.Delete an employee record")
    print("6. Exit")
    option=int(input("Enter your option: "))
    if(option==1):
        employee_id=int(input("Enter your employee ID: "))
        name=input("Enter your name: ")
        position=input("Enter your position: ")
        salary=int(input("Enter your salary: "))
        file.write(f"{employee_id},{name},{position},{salary}\n")
    elif(option==2):
        file.seek(0)
        print(file.read())
    elif(option==3):
        file.seek(0)
        a = file.readlines()
        ID=input("Enter the id: ")
        for i in a:
            b=i.split(',')
            if ID==b[0]:
                print(i)
                break
        else:
            print("Not found")
    elif(option==4):
        employee_id=input("Enter your employee ID: ")
        name=input("Enter your name: ")
        position=input("Enter your position: ")
        salary=int(input("Enter your salary: "))
        file.seek(0)
        a=file.readlines()
        new = []
        for i in a:
            b=i.split(',')
            if employee_id==b[0]:
                new.append(f"{employee_id},{name},{position},{salary}")
            else:
                new.append(i)
        file.seek(0)
        file.truncate(0)
        file.writelines(new)
    elif(option==5):
        employee_id=input("Enter your id: ")
        file.seek()
        a=file.readlines()
        for i in a:
            b=i.split()
            if employee_id==b[0]:
                pass
            else:
                file.append(i)
    elif(option==6):
        file.close()
        break




