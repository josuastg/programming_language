class Vehicle:
    def __init__(self, speed, numberOfWheels):
        self.speed = speed
        self.numberOfWheels = numberOfWheels
    
    def display(self):
        print('Detail')
        print('Kendaraan Roda {} ini dapat memiliki kecepatan {} km/h'.format(self.numberOfWheels, self.speed))

class MotorCycle(Vehicle):
    def __init__(self, name, speed, numberOfWheels):
        self.name = name
        super().__init__( speed, numberOfWheels)    

    def displayMotorcycle(self):
        print("Nama Motor")
        print(self.name)
        super().display()   



ducati = MotorCycle("DUCATI", 150, 2);
ducati.displayMotorcycle();