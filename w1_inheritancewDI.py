class CarAttribute:
    def __init__(self, type, engine, wheel, color):
        self.type = type
        self.engine = engine
        self.wheel = wheel
        self.color = color

    def actribute(self):
        print("{} had {} engine, {} wheel , color is {} ".format( self.type, self.engine, self.wheel, self.color))

class DistanceMove:
    def __init__(self, localtion ,speed, hour):
        self.localtion = localtion
        self.speed = speed
        self.hour = hour
        self.totalrun = self.hour*self.speed

    def actives(self):
        print("This car move in {}. Distance had run is {} km ".format(self.localtion, self.totalrun))

class Car(CarAttribute,DistanceMove):
    def __init__(self, type, engine, wheel, color, localtion ,speed, hour):
        CarAttribute.__init__( self,type, engine, wheel, color),
        DistanceMove.__init__( self,localtion ,speed, hour)

if __name__ == "__main__":        
    car1 = Car("Normal Car","Normal", 4, "green","HaNoi", 60, 40)
    car1.actribute()
    car1.actives()
