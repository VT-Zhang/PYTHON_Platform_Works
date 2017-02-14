class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15

    def display_all(self):
        print "This car is priced at $"+str(self.price)+" and running at "+self.speed+" and the tank is "+self.fuel+" and the mpg is "+self.mileage+" with the tax rate of "+str(self.tax)+"."


car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(2000, "5mph", "No Full", "105mpg")
car3 = Car(2000, "15mpg", "Kind of Full", "95mpg")
car4 = Car(2000, "25mpg", "Full", "25mpg")
car5 = Car(2000, "45mpg", "Empty", "25mpg")
car6 = Car(20000000, "35mpg", "Empty", "15mpg")


print car1.display_all()
print car2.display_all()
print car3.display_all()
print car4.display_all()
print car5.display_all()
print car6.display_all()
