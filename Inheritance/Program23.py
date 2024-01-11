#Method Resolution Order(MRO)

class Boss:

    def report(self):
        print("I am the Boss")

class Manager(Boss):

    def report(self):
        print("Manager:Report to Boss")

class TeamLead(Manager,Boss):

    def report(self):
        print("TeamLead:Report to Boss and Manager")

class Developer(TeamLead):

    def report(self):
        print("Developer:Report to TeamLead")

print(Developer.__mro__)
