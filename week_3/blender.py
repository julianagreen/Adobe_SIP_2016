class blender():
    def __init__(self, weight, blade_speed, num_set, color, name):
        self.weight = weight
        self.blade_speed = blade_speed
        self.num_set = num_set
        self.color = color
        self.name = name

    def turn_on(self):
        print(self.name + " the blender just turned on!")

    def turn_off(self):
        print(self.name + " the blender just turned off!")

    def change_settings(self, setting):
        print(self.name + " the blender just changed to setting" + setting)

    def hold_stuff(self, ingredients):
        print(self.name + " the blender is holding" + ingredients)

vitamix = blender(64, 15, 10, "black", "Billy")
vitamix.turn_on()
vitamix.
