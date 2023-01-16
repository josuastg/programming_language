class Vehicle:
    def display(self):
        print('This is Vehicle')


class MotorCycle(Vehicle):
    def display(self):
        print("This is Vehicle Motorcycle") 

class Bus(Vehicle):
    def display(self):
        print("This is Vehicle Bus") 


motor = MotorCycle()
motor.display()

bus = Bus()
bus.display()