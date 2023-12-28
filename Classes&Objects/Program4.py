class Employee:
    CompName = "Facebook" 
    def __init__(self):
        print("In constructor")
        self.empId = 12
        self.empName = "Kanha"

    def empInfo(self):
        print(self.empId)
        print(self.empName)

emp1 = Employee()
emp2 = Employee()

emp1.empInfo()
emp2.empInfo()
