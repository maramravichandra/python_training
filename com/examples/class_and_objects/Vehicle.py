class Vehicle:
    speed = 0
    started = False
    name = ''
    vehicle_Type = ''

    def __init__(self, name = '', speed=5):
        self.name = name
        print("{} has been named as {}".format(self.vehicle_Type, name))

    def start(self):
        self.started = True
        print(f"{self.vehicle_Type} has been started.")

    def increase_accelaration(self, speed):
        self.speed = self.speed + speed
        print("Speed has been increased by {}".format(speed))


    def print_type(self):
        print("Vehicle Type : ", self.vehicle_Type)

    def stop(self):
        self.speed = 0
        self.started = False
        print(f"{self.vehicle_Type} has been stopped.")