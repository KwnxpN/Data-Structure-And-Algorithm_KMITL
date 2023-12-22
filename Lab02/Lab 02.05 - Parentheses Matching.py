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

    def get_stacktop(self):
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

def is_parentheses_matching(notation):
    """check if parentheses is matching"""
    stack = ArrayStack()
    for char in notation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            stack.pop()
    couple = notation.count("(") == notation.count(")")
    print("Parentheses in {} are {}".format \
          (notation, "matched" if stack.is_empty() and couple else "unmatched"))
    print(stack.is_empty() and couple)
is_parentheses_matching(str(input()))
