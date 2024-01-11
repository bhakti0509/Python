class Boss:

    def report(self):
        print("I'm the Boss")

class Manager1(Boss):

    def report(self):
        print("Report : Manager1")

class Manager2(Boss):

    def report(self):
        print("Report : Manager2")

class Manager3(Boss):
    
    def report(self):
        print("")
class TeamLead1(Manager2, Manager1):

    def report(self):
        print("Report : TeamLead1")

class TeamLead2(Manager2, Manager1):

    def report(self):
        print("Report : TeamLead2")

class Developer(TeamLead1, TeamLead2):

    def report(self):
        print("Report : Developer")
        
obj = Developer()
print(Developer.__mro__)
