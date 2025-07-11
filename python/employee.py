class Employee:
 def __init__(self , empId =None, name=None, salary=None):
        self.__empId = empId
        self.name = name
        self.__salary = salary

def get_emp_details(self):
 print(f"ID: {self.__empId}, Name: {self.name}, Salary: {self.__salary}")
 
def get_empId(self):
   return self.__empId

def set_empId(self, empId):
   self.__empId = empId

class Manager(Employee):
    def __init__(self,empId,name,salary,managerId):
       super().__init__(empId,name,salary)
       self.managerId = managerId

    def get_manager_details(self):
       self.get_emp_details()
       print(f"Manager ID: {self.managerId}")

empobj = Employee(101, "John Doe", 50000.34)
empobj.get_emp_details()
managerobj = Manager(111,'Sunita',45539.34,33)
managerobj.__empId=789
print(managerobj._empId)