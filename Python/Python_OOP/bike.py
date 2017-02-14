class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        miles = 0

    def displayInfo(self):
        print "This bike is priced at ",self.price," with the max speed at ",self.max_speed," and with total miles of ",self.miles,"."

    def ride(self):
        self.miles += 10
        print "Riding, total miles is now: ",self.miles
        return self

    def reverse(self):
        if self.miles < 5:
            self.miles = 0
        else:
            self.miles -= 5
        print "Reversing, total miles is now: ",self.miles
        return self


bike1 = Bike(200, "25mph", 1000)
bike2 = Bike(100, "12mph", 500)
bike3 = Bike(50, "10mph", 300)

print bike1.ride().ride().ride().reverse().displayInfo()
print bike2.ride().ride().reverse().reverse().displayInfo()
print bike3.reverse().reverse().reverse().displayInfo()
