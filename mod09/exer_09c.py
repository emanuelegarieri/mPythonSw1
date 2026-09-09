import random

class Car:
    def __init__ (self, reg_num, maximum_speed):
        self.license_plate = reg_num
        self.max_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0.0
        
    def accelerate(self, change):
        if self.current_speed + change >= self.max_speed:
            self.current_speed = self.max_speed
    
        elif self.current_speed + change <= 0:
            self.current_speed = 0
    
        else:
            self.current_speed += change
    
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


    import random


    def race(cars):
        while all(car.travelled_distance < 10000 for car in cars):

            for car in cars:
                speed_change = random.randint(-10, 15)

                car.accelerate(speed_change)
                car.drive(1)

        return cars