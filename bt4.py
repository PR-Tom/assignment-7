import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
cars = []
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    car = Car(f"ABC-{i}", max_speed)
    cars.append(car)
race_over = False
hours = 0
while not race_over:
    hours += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10_000:
            race_over = True
print(f"\nRace finished after {hours} hours\n")
print(f"{'Reg No.':<10}{'Max Speed':<12}{'Speed':<10}{'Distance':<12}")
print("-" * 44)
for car in cars:
    print(f"{car.registration_number:<10}"
          f"{car.max_speed:<12}"
          f"{car.current_speed:<10}"
          f"{car.travelled_distance:<12}")