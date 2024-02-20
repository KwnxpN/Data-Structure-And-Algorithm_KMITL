"""KKK"""

class Student:
    """student"""
    def __init__(self, std_id, name, gpa):
        """con"""
        self.__std_id = std_id
        self.__name = name
        self.__gpa = "%.2f"%gpa
    def get_std_id(self):
        """std id getter"""
        return self.__std_id
    def get_name(self):
        """name getter"""
        return self.__name
    def get_gpa(self):
        """gpa getter"""
        return self.__gpa
    def print_detail(self):
        """print details"""
        print("ID: {}".format(self.get_std_id()))
        print("Name: {}".format(self.get_name()))
        print("GPA: {}".format(self.get_gpa()))

def main(text_in):
    """main"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()
main(input())
