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
        self.head = None
        self.count = 0

    def traverse(self):
        if not self.head:
            print("This is an empty list.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print()

    def insert_last(self, data):
        new_node = DataNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_before(self, node_data, data):
        if not self.head:
            print("Cannot insert, list is empty.")
            return

        new_node = DataNode(data)

        if self.head.data == node_data:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return

        current = self.head
        while current.next and current.next.data != node_data:
            current = current.next

        if not current.next:
            print(f"Cannot insert, {node_data} does not exist.")
            return

        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def delete(self, data):
        if not self.head:
            print(f"Cannot delete, {data} does not exist.")
            return

        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            print(f"Cannot delete, {data} does not exist.")
            return

        current.next = current.next.next
        self.count -= 1