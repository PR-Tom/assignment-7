class Car:
    def __init__(self, max_speed):
        self.speed = 0
        self.max_speed = max_speed

    def accelerate(self, change):
        self.speed += change

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

car = Car(180)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Current speed:", car.speed, "km/h")
car.accelerate(-200)
print("Final speed:", car.speed, "km/h")