"""KKK"""

class Elevator:
    """We are building the elevator"""
    def __init__(self, max_floor):
        """get the max_floor of this building"""
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """the passenger select the floor"""
        self.current_floor = floor

    def show_current_floor(self):
        """wehre is elevator now"""
        print(self.current_floor)

def elevator_is_going_up_and_down(maximum):
    """chipichipichapadubidubidubaduba"""
    elevator = Elevator(maximum)
    next_floor = str(input())
    while next_floor != "Done":
        next_floor = int(next_floor)
        if next_floor <= maximum:
            elevator.go_to_floor(next_floor)
        else:
            print("Invalid Floor!")
        next_floor = str(input())
    elevator.show_current_floor()
elevator_is_going_up_and_down(int(input()))
