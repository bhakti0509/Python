'''
WAP in which you have to write a __new__ user-defined function that creates a new instance of a class

'''

class Employee:

    compName = 'Google'

    def __new__(self):

        print("Object creation done!")

    def __init__(self):
        
        self.empId = 101
        self.empName = 'Bhakti'
        print("Instance variables intialized successfully!")

    def empInfo(self):

        print(self.empId)
        print(self.empName)

obj = Employee()
obj.empInfo()
