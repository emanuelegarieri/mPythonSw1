import random


class Car:
    def __init__ (self, reg_num, maximum_speed):
        self.license_plate = reg_num
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0.0
        
    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
    
        elif self.current_speed + change <= 0:
            self.current_speed = 0
    
        else:
            self.current_speed += change
    
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars


    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
        return


    def print_status(self):
        for c in self.cars:
            print(c.license_plate)
            print(c.travelled_distance)
        return


    def race_finished(self):
        for c in self.cars:
            if c.travelled_distance >= self.distance:
                return True
        return False



