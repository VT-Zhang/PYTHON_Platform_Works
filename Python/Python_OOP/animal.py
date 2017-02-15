class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        str1 = self.name + " now has "+str(self.health)+" health."
        return str1

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        newStr = "This is the Dragon " + super(Dragon, self).displayHealth()
        return newStr

animal = Animal("animal")
animal.walk().walk().walk().run().run()
print animal.displayHealth()
dog = Dog("dog")
dog.walk().walk().walk().run().run().pet()
print dog.displayHealth()
dragon = Dragon("dragon")
dragon.walk().walk().walk().run().run().fly().fly()
print dragon.displayHealth()
