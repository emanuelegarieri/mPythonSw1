class Car:
    def __init__ (self, reg_num, maximum_speed):
        self.license_plate = reg_num
        self.max_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        
    def accelerate(self, change):
        if self.current_speed + change >= self.max_speed:
            self.current_speed = self.max_speed
    
        elif self.current_speed + change <= 0:
            self.current_speed = 0
    
        else:
            self.current_speed += change
    
car = Car("ABC-123", 142)
