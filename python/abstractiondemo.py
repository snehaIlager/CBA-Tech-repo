from abc import ABC,abstractmethod
class Empl(ABC):
    @abstractmethod
    def cal_salary():
        pass

class Accountant(Empl):
    def __init__(self,salary):
        self.salary = salary

    def cal_salary(self):
        return 0.10*self.salary+self.salary
    
accountant = Accountant(54000.34)
print(accountant.cal_salary)