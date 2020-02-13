class Employee:
    # this is a global variable
    employeeCount = 0

    def __init__(self,name,age,salary):
        
        self.name = name
        self.age = age
        self.salary = salary
        Employee.employeeCount + 1

    def displayCount(self):
        print("Total No of Employee",Employee.employeeCount)
    
    def displayEmployeeSelf(self):
        print("Employee Name :",self.name,",Salary :",self.salary,", Age :",self.salary)


