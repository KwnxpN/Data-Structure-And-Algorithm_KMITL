"""KKK"""

class Person:
    """Person Human Humanity FREEDOM"""
    def __init__(self, name, age):
        """attribute"""
        self.name = name
        self.age = age
    def get_detail(self):
        """info of this person"""
        print(self.name+",", self.age, "years old")
    def say_hello(self):
        """HELLLLOOOOOO"""
        return "Hello, my name is "+ self.name+"!"

class Project:
    """Project group"""
    def __init__(self, project_name, members, our_team):
        self.project_name = project_name
        self.members = members
        self.our_team = our_team
    def show_project_name(self):
        """show project name"""
        print("Hello There! This is "+self.project_name)
    def show_members(self):
        """show members here"""
        print("This project has", self.members, "members")
        for member in self.our_team:
            print(member.say_hello())

def main(name_of_project, members_amount):
    """main"""
    our_team = sorted([Person((str(input())), int(input())) for _ in range(members_amount)], \
                      key=lambda self: self.name)
    project = Project(name_of_project, members_amount, our_team)
    project.show_project_name()
    project.show_members()
main(str(input()), int(input()))
 