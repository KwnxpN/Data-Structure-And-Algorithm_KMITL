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
def main():
    """main"""
    stack = ArrayStack()

    stack.push("100")
    stack.push(100)
    stack.push("3.14")
    stack.push(3.14)
    stack.push("66.4a")
    stack.push("Ackerman")

    stack.print_stack()

    print(stack.get_size())
    var1 = stack.pop()
    print(var1)
    stack.print_stack()
    print(stack.get_size())

    while not stack.is_empty():
        print(stack.pop())

    print()
    print(stack.pop())
    print(stack.get_stacktop())
    print(var1)
main()
