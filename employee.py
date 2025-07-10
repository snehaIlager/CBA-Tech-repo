class Employee:
 def __init__(self , empId =None, name=None, salary=None):
        self.__empId = empId
        self.name = name
        self.__salary = salary

def get_emp_details(self):
 print(f"ID: {self.__empId}, Name: {self.name}, Salary: {self.__salary}")
 

class Manager(Employee):
    def__init__(self,managerId):
    self.managerId = managerId
 empobj = Employee(101, "John Doe", 50000)

 empobj.get_emp_details()