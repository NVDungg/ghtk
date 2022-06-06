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


#Composition 
class Car:
    def __init__(self, type, engine, wheel, color, localtion, speed, hour):
        self.obj1 = CarAttribute( type, engine, wheel, color)
        self.obj2 = DistanceMove( localtion, speed, hour)

    def infomations(self):
        print(f"{self.obj1.type} can go in {self.obj2.localtion}")
        self.obj1.actribute()
        self.obj2.actives()


if __name__ == "__main__":        
    car1 = Car("Normal Car","Normal", 4, "green","HaNoi", 60, 40)
    car1.infomations()

    car2 = Car("Super Car","Normal", 4, "green","Thuong Tin",80, 9)
    car2.infomations()
        
#Aggregation
"""class Car:
    def __init__(self, acc, att):
        self.obj1 = acc;
        self.obj2 = att

    def infomations(self):
        self.obj1.actribute()
        self.obj2.actives()

if __name__ == "__main__":
    att1 = CarAttribute("Normal Car","Normal", 4, "green")
    acc1 = DistanceMove("HaNoi",60, 40)
    car1 = Car(att1,acc1)
    car1.infomations()

    att2 = CarAttribute("Super Car","Normal", 4, "green")
    acc2 = DistanceMove("Thuong Tin",80, 9)
    car2 = Car(att2,acc2)
    car2.infomations()"""

