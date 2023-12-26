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
        print("Hello, my name is "+ self.name+"!")

def main():
    """main here"""
    person = Person(str(input()), int(input()))
    person.get_detail()
    person.say_hello()
main()
