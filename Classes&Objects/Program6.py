class Company:
    compName = "Facebook";

    def __init__(self):
        print("In constructor")
        self.empId = 12
        self.empName = "Kanha"

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        #print(self.compName)
        print(Company.compName)

emp1 = Company()
emp1.compInfo()
