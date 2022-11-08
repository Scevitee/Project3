# Proj 3 involves sorting

class TeachingAssistant:
    hourly_pay = 13

    def __init__(self, name, email="admin@ufl.edu", working_hours=0):
        self.name = name
        self.email = email
        self.working_hours = working_hours

    def run_discussion(self, hours):
        pass

    def weekly_pay(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.email} - {self.working_hours}"

    def __repr__(self):
        return f"{self.name} - {self.email} - {self.working_hours}"

    def __eq__(self, other):
        if isinstance(other, TeachingAssistant):
            return self.email == other.email

    def __lt__(self, other):
        if isinstance(other, TeachingAssistant):
            return self.name < other.name  #sorts in ascending order


ta1 = TeachingAssistant("Oscar", "oscar123@ufl.edu", 1)
ta2 = TeachingAssistant("Maya", "maya083@ufl.edu", 0)
ta3 = TeachingAssistant("Logan", "logan87@ufl.edu", 2)

###we will use __lt__ to sort in proj 3

tas = [ta1, ta2, ta3]
print(tas)

# 1st sorting approach using __lt__ operator
# tas.sort()
# print(tas)


# 2nd approach
tas.sort(key=lambda ta: ta.name)
print(tas)


#### Stuff for Project 3

## pakuri.py

# go from pakuri -> pakudex -> pakuri_program

