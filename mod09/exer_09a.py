class Car:
    def __init__ (self, reg_num, maximum_speed):
        self.license_plate = reg_num
        self.max_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
car = Car("ABC-123", 142)

print(f"License plate: {car.license_plate} \n" +
      f"Maximum speed: {car.max_speed} km/h \n" +
      f"Current speed: {car.current_speed} km/h \n" +
      f"Travelled distance: {car.travelled_distance} km")