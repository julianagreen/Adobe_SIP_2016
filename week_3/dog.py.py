class Dog():

    #constructor function
    def __init__(self, furColor, weight, eyeColor):
        self.furColor = furColor
        self.weight = weight
        self.eyeColor = eyeColor

    #function
    def bark(self):
        print("Woof")

    def wag(self):
        print("Wagging Tail")

    def run(self):
        print("Your dog is running away")


Toto = Dog("Brown", 25, "Blue", "Toto")

Toto.bark()