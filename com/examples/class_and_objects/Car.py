from com.examples.class_and_objects.Vehicle import Vehicle


class Car(Vehicle):
    vehicle_Type = 'Car'
    speed = 10

    def increase_accelaration(self, speed):
        if not self.started:
            print("Car is not started. You can't increase the speed")
        else:
            super().increase_accelaration(speed)


class Motorbike(Vehicle):
    vehicle_Type = 'Motorbike'

class Bus(Vehicle):
    vehicle_Type = 'Bus'

# variable_name = <Class Name>()
car = Car()
car.increase_accelaration(10)
car.stop()
car.print_type()

bus = Bus()
bus.start()
bus.increase_accelaration(10)
bus.stop()
bus.print_type()

car1 = Car()
print( id(car1))
car2 = Car("Honda")
print( id(car2))

print("Is Same Objects ? ", car1 == car2)

motorbike = Motorbike()
motorbike.print_type()

bus = Bus()
bus.print_type()

