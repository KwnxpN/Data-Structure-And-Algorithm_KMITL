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

def main():
    """main is here"""
    data_node = DataNode(str(input()))
    print(data_node.get_data())
    print(data_node.get_next())
main()
