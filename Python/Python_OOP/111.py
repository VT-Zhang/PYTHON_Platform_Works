class Human(object):
    def __init__(self, hairColor, height):
        self.hairColor = hairColor
        self.height = height
        self.energy = 100

    def walk(self):
        print "I'm walking."
        self.energy -= 10
        print self.energy
        return self

# tim = Human("black", 72)
jack = Human("brown", 70)
#
# print tim.height
print jack.walk()

class Athlete(Human):
    def __init__(self, hairColor, height):
        super(Athlete, self).__init__(hairColor, height)
        print self.energy
        self.energy = 200
jason = Athlete("Black", 72)
print jason
