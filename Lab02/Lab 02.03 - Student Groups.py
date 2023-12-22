"""KKK"""

class ArrayStack:
    """Array Stack"""
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        """push data to stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """pop data from stack"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            pop_num = self.data.pop()
            self.size -= 1
            return pop_num

    def is_empty(self):
        """check if the stack is empty"""
        return True if self.data == [] else False

    def get_stack_top(self):
        """get the top value of stack"""
        if self.data == []:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self):
        """get the size of stack"""
        return len(self.data)

    def print_stack(self):
        """print the stack"""
        print(self.data)

def student_groups(group_num, student_amount):
    """group all the student by pop from stack"""
    stack = ArrayStack()
    for _ in range(student_amount):
        stack.push(str(input()))
    student_dict = dict((i, []) for i in range(1, group_num+1))
    while stack.is_empty() == False:
        for i in range(1, group_num+1):
            if stack.get_size() == 0:
                break
            else:
                student_dict[i].append(stack.pop())
    for group, students in student_dict.items():
        print("Group {}: ".format(group), end="")
        print(*students, sep=", ")
student_groups(int(input()), int(input()))
