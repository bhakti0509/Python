class Manager:

    def Project(self):
        print("In project: Manager")

class TeamLead1(Manager):
    pass

class TeamLead2(Manager):
    def Project(self):
        print("In project: TeamLead2")

class Developer(TeamLead1, TeamLead2):
    pass

obj1 = Developer()
obj1.Project()

