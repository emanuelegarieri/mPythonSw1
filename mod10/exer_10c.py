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


class Building:
    def __init__(self, bottom, top, elevator):
        self.bottom_floor = bottom
        self.top_floor = top
        self.elevators = [] 
        for _ in range(elevator):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, elevator, floor):
        self.elevators[elevator].go_to_floor(floor)


    def fire_alarm(self):
        for e in self.elevators:
            e.go_to_floor(self.bottom_floor)