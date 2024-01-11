"""KKK"""

class DataNode:
    """Creat Datanode in singly linked lists"""

    def __init__(self, data=None):
        """Attribute"""
        self.__data = data
        self.__next = None
    def get_data(self):
        """return data"""
        return self.__data
    def set_data(self, data):
        """set new data"""
        self.__data = data
    def get_next(self):
        """return next"""
        return self.__next
    def set_next(self, _next):
        """set new next"""
        self.__next = _next

class SinglyLinkedList:
    """singly linked list"""
    def __init__(self):
        """init"""
        self.count = 0
        self.head = None

    def insert_last(self, data):
        """insert last"""
        pnew = DataNode(data)
        if self.head is None:
            self.head = pnew
        else:
            start = self.head
            while start.get_next() is not None:
                start = start.get_next()
            start.set_next(pnew)
        self.count += 1
    def insert_front(self):
        """insert front"""
        pass
    def insert_before(self):
        """insert before"""
        pass
    def traverse(self):
        """traverse"""
        if self.head is None:
            print("This is an empty list.")
        else:
            start = self.head
            while start.get_next() is not None:
                print(start.get_data(), end=" -> ")
                start = start.get_next()
            print(start.get_data())

def main():
    """main here"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()
