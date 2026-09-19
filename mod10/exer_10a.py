class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.current_floor = bottom
        self.top_floor = top

    def floor_up(self):
        self.current_floor += 1
        print(f"Floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Floor: {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if floor > self.current_floor:
                self.floor_up()
            else: 
                self.floor_down()
