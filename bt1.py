class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


def main():
    car = Car("ABC-123", 142)

    print("Registration number:", car.registration_number)
    print("Maximum speed:", car.max_speed, "km/h")
    print("Current speed:", car.current_speed, "km/h")
    print("Travelled distance:", car.travelled_distance, "km")


main()